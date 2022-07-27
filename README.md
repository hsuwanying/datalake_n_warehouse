### Treavelling digital journey insights analysis & data visualization
Design and develop a travel data warehouse and traveler-insight dashboard with the use of Instagram and Google trend data, which aims to help Swiss travel service providers to better understand and capture digital travelers’ preference.

#### Data Piplines:

- Airflow Dag:
  - callapi.py: DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

- Python & Jupyter Notebook:
  - List_of_Zip_code_Switzerland.ipynb: zip_code.csv data clearning and loading to RDS_PostgreSQL
  - my_switzerland_API.ipynb: Fetching destination information with the use of MySwitzerland API
  - Insta_create_hashtag.ipynb: Fetching Instagram hashtag media informations with the use of Instagram Graph API

#### Visualization
A visual dashboard is created by using Tableau. It gives key metries about travel destination in Switzerland. The dashboard can be access via: https://public.tableau.com/app/profile/yang7231/viz/Dashboard_final_16402072757680/FinalDashboard?publish=yes
