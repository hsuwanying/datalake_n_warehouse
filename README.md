# Discovering the Immstagramable destinations in Switzrerland: A Traveller Insights analysis from Data Collection to Data Visualization
This project aims to build a travel data warehouse and create an insight dashboard that helps Swiss OTAs to optimize online booking expereince with the use of social media and search engine data.

This group project is submitted as part of assignemnt for Data Warehousing and Data Lake module for MSc in [IDS](https://www.hslu.ch/en/lucerne-school-of-business/degree-programmes/master/applied-information-and-data-science/) at [HSLU](https://www.hslu.ch/de-ch/)

# Authors
 - [Carol Hsu](https://github.com/hsuwanying) 
 - [Cheuh Yang](https://github.com/cyyang50)

# Table of Content
 - [Background](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#initial-situation)
 - [Business Problem](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#business-problem)
 - [Solution](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#solution)
 - [Data Source](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-source)
 - [Data Architecture](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-architecture)
 - [Prototype](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#prototype)
 - [Conclusion](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#conclusion)
 - [Project Reflection](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#project-reflection)
 - [Notebook](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#notebook)
 - [Reference](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#reference)

# Background
In recent years, social media such as Instagram, Facebook, Twitter, and Tiktok have significantly influenced people’s behavior toward their choices and decision-making. This phenomenon is even more visible in fields involving many human interactions, such as fashion, retailing, and travel businesses. 

# Business Problem
When reviewing travel websites, many travel-related websites are more or less product-driven; they follow a traditional approach, that is, the majorities of travel websites focus on promoting travel packages, products, and tourist spots, with less addressing of what customers are genuinely interested in. Travel service providers shall help end users to give recommendations that help them create memorable travel experiences during their holiday, make a positive online presence, and provide a better travel experience to tourists.

**Business Questions 1**:
“How can we improve tourist travel experience in Switzerland by utilizing social media and search engine data? “
1. What are the popular destinations in Switzerland that people search for travelling?
2. Which city do people are interested the most in Switzerland?

**Business Questions 2**:
“How do individuals and businesses utilize social media hashtags to boost their online presence and performance?”
1. What are the popular hashtags (top 5) used in Switzerland?
2. What are the popular hashtags (top 5) based on Swiss canton or city or destinations
name?

**Business Questions 3**:
“Is there any relation between the use of travel hashtags in social media, and keywords search?”
Does google search result influence people to use certain hashtags for their posts?
Hypothesis: The more google search in particular location, the more hashtag of the location will be used in post.

# Solution
The goal of this project is to help Swiss OTAs and marketers understand the roles they play at each phase and the opportunities that inspire travelers to complete a travel booking. In this project, we designed a data lake and data warehouse system that allow us to use it as the foundation for developing an entertainment application for travel destination hunts. It helps people to discover the trendiest spots while traveling in Switzerland.

# Data Source
1. Instagram media data via [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/)
 - media post time
 - media type
 - caption
 - mentions
 - hashtags 
 - no. of likes, 
 - no. comments
2. MySwitzerland: [Switzerland Tourism | OpenData API](https://developer.myswitzerland.io)
 - destination identifier
 - attractions identifier
 - geopoint
  - longitude
  - latitude
3. Die Post: [Address web services REST](https://developer.post.ch/en/address-web-services-rest)
 - Post code
 - Kantons and cities' names in English, German and Franch
 - Short Code

# Data Architecture
<img width="893" alt="Screenshot 2022-08-30 at 22 09 27" src="https://user-images.githubusercontent.com/72688726/187533413-9f9aec3c-7b5d-441f-ba11-5c0e9aaa7494.png">

## Data Pipeline Construction: Instagram Hashtag Information
There are three phases of fetching data from Instagram. 
 1) Preparing database and create tables for storing data 2) Fetching data & Feature extraction, and 3) data manipulation.

# Data Anlysis
IG Hashtag Statistic gives information about the usage of hashtags in each Instagram post. Posts with hashtag Zurich receives the most likes which has 169’235 likes and 6’170 comments among Switzerland, In the same period, Valais and Luzern are the second and the third place, with 144’957 and 120’267 likes. Then we look at the donut chart, Zurich Wallis and Uri are the most popular cantons and Zurich, Zermatt, Interlaken are the most admired cities. Therefore, we can conclude, Zurich is the most popular and most visited place among Switzerland.

<img width="838" alt="tags" src="https://user-images.githubusercontent.com/72688726/187530598-4457abd1-1ca8-452a-a5ec-129c52f2126b.png">

# Prototype
A visual dashboard is created by using Tableau. It gives key metries about travel destination in Switzerland. 

The dashboard can be seen in 
[Tableau Public](https://public.tableau.com/app/profile/yang7231/viz/Dashboard_final_16402072757680/FinalDashboard?publish=yes)

# Conclusion
The design of the database helps us to realize the information that are obtained from both Google trend and Instagram. By establishing analysis requirements, we are able to generate insights that can answer our business questions. Since we do not have data from the user side, the dashboard is more focus on the value creation to business providers such as online travel agents and marketing firms, so that can utilize matrixes from this dashboard, to provide more personalized service and product to travelers.

# Project Reflection
It was a great experience to applied my past expereince in Business design and Customer experience into digital product design. From this course, I have learnd many hard skill from the data engeneering field, We had chance to apply knowledge and utilized popular tools such as AWS and Airflow to realize our buisness idea within three months. It was pretty stresseful to work on a big project within such a short time (meanwhile writting a master thesis), neverthless, the gains of this module was tremendous.

# Notebook
  - Airflow Dag:
    - callapi.py: DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

  - Python & Jupyter Notebook:
    - List_of_Zip_code_Switzerland.ipynb: zip_code.csv data clearning and loading to RDS_PostgreSQL
    - my_switzerland_API.ipynb: Fetching destination information with the use of MySwitzerland API
    - Insta_create_hashtag.ipynb: Fetching Instagram hashtag media informations with the use of Instagram Graph API
