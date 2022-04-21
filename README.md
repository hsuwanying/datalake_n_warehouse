### datalake_warehouse
Design and develop a travel data warehouse and traveler-insight dashboard with the use of Instagram and Google trend data

#### Data Piplines:

- Airflow Dag:
  - call_api.py: DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

- Python & Jupyter Notebook:
  - List_of_Zip_code_Switzerland.ipynb: zip_code.csv data clearning and loading to RDS_PostgreSQL
  - my_switzerland_API.ipynb: Fetching destination information with the use of MySwitzerland API
  - Insta_create_hashtag.ipynb: Fetching Instagram hashtag media informations with the use of Instagram Graph API
