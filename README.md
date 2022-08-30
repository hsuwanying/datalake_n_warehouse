# Discover the Immstagramable destinations in Switzrerland
Improving Swiss OTAs online booking experience by analysing social media and search engine data to generate insights into traveller insights

This project is submitted as part of assignemnt for Data Warehousing and Data Lake module for MSc in [IDS](https://www.hslu.ch/en/lucerne-school-of-business/degree-programmes/master/applied-information-and-data-science/) at [HSLU](https://www.hslu.ch/de-ch/)

# Author
[Carol Hsu](https://github.com/hsuwanying)

# Table of Content
 - [Background](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#initial-situation)
 - [Business Problem](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#business-problem)
 - [Solution](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#solution)
 - [Business Design](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#business-design)
 - [Data Source](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-source)
 - [Methods](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#Methods)
 - [Data Architecture](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-architecture)
 - [Data Analysis](https://github.com/hsuwanying/traveller-insights-analysis/main/README.md#data-analysis)
 - [Prototype](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#prototype)
 - [Conclusion](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#conclusion)
 - [Project Reflection](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#project-reflection)
 - [Notebook](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#notebook)
 - [Reference](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#reference)

# Background
# Business Problem
# Solution
# Business Design
# Data Source
# Methods
# Data Architecture
  ## Data Piplines
# Data Analysis
# Prototype
A visual dashboard is created by using Tableau. It gives key metries about travel destination in Switzerland. 

The dashboard can be seen in 
[Tableau Public](https://public.tableau.com/app/profile/yang7231/viz/Dashboard_final_16402072757680/FinalDashboard?publish=yes)

# Conclusion
# Project Reflection
# Notebook
  - Airflow Dag:
    - callapi.py: DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

  - Python & Jupyter Notebook:
    - List_of_Zip_code_Switzerland.ipynb: zip_code.csv data clearning and loading to RDS_PostgreSQL
    - my_switzerland_API.ipynb: Fetching destination information with the use of MySwitzerland API
    - Insta_create_hashtag.ipynb: Fetching Instagram hashtag media informations with the use of Instagram Graph API

# Project Reflection
