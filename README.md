# Discovering the Immstagramable destinations in Switzrerland: A Traveller Insights analysis from Data Collection to Data Visualization
This project aims to build a travel data warehouse and create an insight dashboard that helps Swiss OTAs to optimize online booking expereince with the use of social media and search engine data.

This group project is submitted as part of assignemnt for Data Warehousing and Data Lake module for MSc in [IDS](https://www.hslu.ch/en/lucerne-school-of-business/degree-programmes/master/applied-information-and-data-science/) at [HSLU](https://www.hslu.ch/de-ch/)

# Authors
[Carol Hsu](https://github.com/hsuwanying)
[Cheuh Yang](https://github.com/cyyang50)

# Table of Content
 - [Background](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#initial-situation)
 - [Business Problem](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#business-problem)
 - [Solution](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#solution)
 - [Data Source](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-source)
 - [Data Architecture](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-architecture)
 - [Data Analysis](https://github.com/hsuwanying/traveller-insights-analysis/main/README.md#data-analysis)
 - [Prototype](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#prototype)
 - [Conclusion](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#conclusion)
 - [Project Reflection](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#project-reflection)
 - [Notebook](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#notebook)
 - [Reference](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#reference)

# Background
In recent years, social media such as Instagram, Facebook, Twitter, and Tiktok have significantly influenced people’s behavior toward their choices and decision-making. This phenomenon is even more visible in fields involving many human interactions, such as fashion, retailing, and travel businesses. 

## Traveller Statistic
 - About 67% of people confirmed they use social media, especially Instagram to get inspiration for planning their next dream place to travel(Facebook, 2017), 
 - 84% of millennials said they consume social media feeds for particular images and videos.
 - Online search dominates at the beginning stage of a customer’s buying journey(ThinkwithFGoogle, 2016). 
 
# Business Problem
Internet is the starting point at the beginning of a traveler’s decision-making process, which means that searching online is the first thing people would do when they intend t travel. They start to search holiday-related keywords via search engines, then click through links that direct them to the travel provider’s website.

When reviewing travel websites, many travel-related websites are more or less product-driven; they follow a traditional approach, that is, the majorities of travel websites focus on promoting travel packages, products, and tourist spots, with less addressing of what customers are genuinely interested in. Travel service providers shall help end users to give recommendations that help them create memorable travel experiences during their holiday, make a positive online presence, and provide a better travel experience to tourists.

# Solution
The goal of this project is to help Swiss OTAs and marketers understand the roles they play at each phase and the opportunities that inspire travelers to complete a travel booking. In this project, we designed a data lake and data warehouse system that allow us to use it as the foundation for developing an entertainment application for travel destination hunts. It helps people to discover the trendiest spots while traveling in Switzerland.

# Data Source
1. Instagram media data via [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/)
 - hashtags 
 - no. of likes, 
 - no. comments
2. MySwitzerland: [Switzerland Tourism | OpenData API](https://developer.myswitzerland.io)
 - Destination
 - Attraction
3. Die Post: [Address web services REST](https://developer.post.ch/en/address-web-services-rest)
 - Post code
 - Kantons and cities' names in English, German and Franch
 - Short Code

# Data Architecture
  ## Data Piplines
# Data Analysis
# Prototype
A visual dashboard is created by using Tableau. It gives key metries about travel destination in Switzerland. 
The dashboard can be seen in 
[Tableau Public](https://public.tableau.com/app/profile/yang7231/viz/Dashboard_final_16402072757680/FinalDashboard?publish=yes)

# Conclusion

# Project Reflection
It was a great experience to applied my past expereince in Business design and Customer experience into digital product design. From this course, I have learnd many hard skill from the data engeneering field, We had chance to apply knowledge and utilized popular tools such as AWS and Airflow to realize our buisness idea within three months. It was pretty stresseful to work on a big project within such a short time (meanwhile writting a master thesis), neverthless, the gains of this module was tremendous.

# Notebook
  - Airflow Dag:
    - callapi.py: DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

  - Python & Jupyter Notebook:
    - List_of_Zip_code_Switzerland.ipynb: zip_code.csv data clearning and loading to RDS_PostgreSQL
    - my_switzerland_API.ipynb: Fetching destination information with the use of MySwitzerland API
    - Insta_create_hashtag.ipynb: Fetching Instagram hashtag media informations with the use of Instagram Graph API
