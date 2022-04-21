import requests
import re
import pandas as pd
import pprint
import json
import urllib.request
import urllib.error
from time import gmtime, strftime
import time
from datetime import datetime, timedelta
from time import sleep
import psycopg2
import os.path

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 11, 21),
    'email': ['hsu.carol84@gmail.com'],
    'email_on_failure': False,
    'email_on_delay': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


def callApi():
    instagram_business_account = "instagram_business_account"
    access_token = "access_token"
    domain = "https://graph.facebook.com/v12.0"
    #ig_hashtag_ids=['17843678611020704','17843678038040490','17841562906121517','17843977789033663','17842294453030357'] #for testing
    ig_hashtag_ids = ['17843695108061880','17841562486127746','17843781943053326','17843737147012077','17841563617103035','17843770291063460','17843731063037362','17843674843009135','17843766175034928','17841563632129050','17841563290127743','17841563314095275','17843857468005360','17843794165015026','17841589219074534','17843715058054899','17841594358073046','17841562702112282','17841563410095061','17841549814118642','17843714212014818','17841514093097929','17843668015049047','17843721961051022','17841564079084570','17843678611020704','17843678038040490','17841562906121517','17843977789033663','17842294453030357']
    query_types = ['recent_media','top_media']
    fetch_from_api = 1 # activate api call, incase got block

    #connect to postgres
    conn = psycopg2.connect(host="datalake-1.cyjrpnr3hv9x.us-east-1.rds.amazonaws.com",database="datalake1",user="MVision",password="MVision123")
    cursor = conn.cursor()
    conn.autocommit = True
    now = time.time()
    timeToLive = 3600 # 1 hour

    # looping through a list of hashtags in `ig_hashtag_ids`
    for ig_hashtag_id in ig_hashtag_ids:
        for query_type in query_types:
            filename = query_type+'_'+ig_hashtag_id+'.json' #save file name to chech if all data are load
            print(filename)
            if fetch_from_api: # if fetch_from_api = 1 means is fetching data
                url = f'{domain}/{ig_hashtag_id}/{query_type}?user_id={instagram_business_account}&fields=id,caption,media_type,media_url,permalink,comments_count,like_count,time,timestamp&access_token={access_token}'
                print(url)
                #exit()
                if os.path.isfile(filename) and os.path.getmtime(filename)+timeToLive<now:
                    print('remove file:'+filename)
                    os.remove(filename)
                if os.path.isfile(filename): # check if data can be loaded locally
                    print('file exists:'+filename)
                    with open(filename, 'r') as json_file:
                        data=json_object = json.load(json_file)
                else:
                    print('file does not exist:'+filename) # debug problem hashtag entry
                    print('')
                    #continue

                    with urllib.request.urlopen(url) as url:
                        data = json.loads(url.read().decode())
                    with open(filename, 'w') as f:
                        json.dump(data, f)
                    time.sleep(2) # deactivate api call to avoid getting blocked
            else:
                # get data from file
                if os.path.isfile(filename): # check if data can be loaded locally
                    with open(filename, 'r') as json_file:
                        data=json_object = json.load(json_file)
                else:
                    print('file does not exist:'+filename) # debug problem hashtag entry

            for index, item in enumerate(data['data']):
                like_count = data['data'][index].get('like_count‘, 0)
                caption = data['data'][index].get('caption','')
                timestamp = int(time.mktime(datetime.datetime.strptime(data['data'][index]['timestamp'], "%Y-%m-%dT%H:%M:%S%z").timetuple()))
                # insert post into posts
                sql = "INSERT INTO posts (ig_id,ig_hashtag_id,timestamp,caption,query_type,media_type,permalink_url,comment_count,like_count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (permalink_url) DO NOTHING RETURNING pos_id;"
                row = [
                    data['data'][index]['id'],
                    ig_hashtag_id,
                    timestamp,
                    caption,
                    query_type,
                    data['data'][index]['media_type'],
                    data['data'][index]['permalink'],
                    data['data'][index]['comments_count'],
                    like_count
                ]
                cursor.execute(sql, tuple(row))
                result=cursor.fetchone()
                pos_id=0
                if result and result[0]:
                    pos_id=result[0]
                if pos_id:
                    hashtags = re.findall('[#]([^#\s,.]+)',caption) # using regular expression to seprate hashtag in capition field
                    print(hashtags)
                    for hashtag in hashtags:
                        sql = "SELECT tag_id from public.tags WHERE tag = %s"
                        row2=[hashtag]
                        cursor.execute(sql, tuple(row2))
                        result=cursor.fetchone()
                        tag_id=0
                        if result and result[0]:
                            # get tag id
                            tag_id=result[0]
                        else:
                            # insert new tag into tags
                            sql = "INSERT INTO public.tags (tag) VALUES (%s) RETURNING tag_id"
                            row3=[hashtag]
                            result=cursor.execute(sql, tuple(row3))
                            if result and result[0]:
                                tag_id=result[0]

                        if tag_id:
                            sql = "INSERT INTO public.post_tags (pos_id,tag_id) VALUES (%s,%s)"
                            row4=[pos_id,tag_id]
                            cursor.execute(sql, tuple(row4))

dag = DAG(
    'callApi', default_args = default_args,
    schedule_interval=timedelta(days=1)
)

callApi_task = PythonOperator(
    task_id="callApi",
    python_callable=callApi,
    dag=dag)
