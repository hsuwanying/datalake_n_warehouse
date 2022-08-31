# Discovering the Immstagramable destinations in Switzerland: A traveller insights analysis from data collection to data visualization
### This project aims to build a travel data warehouse and create an insight dashboard that helps Swiss OTAs optimize the online booking experience using social media and search engine data. 

<br>
<p align = "center">
<img src ="https://user-images.githubusercontent.com/72688726/187684537-4684634f-89e6-49a7-82b2-4b912576281a.jpeg">
</p>
<p align = "center">Photo by
<a href="https://user-images.githubusercontent.com/72688726/187684537-4684634f-89e6-49a7-82b2-4b912576281a.jpeg">Devam Jhabak</a> on <a href="https://unsplash.com/s/photos/spam?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</p>
<br>

# Authors
 - [Carol Hsu](https://github.com/hsuwanying) 
 - [Cheuh Yang](https://github.com/cyyang50)
 
# Table of Content
 - [Business Problem](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#business-problem)
 - [Solution](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#solution)
 - [Methods](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#methods)
 - [Data Source](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-source)
 - [Result](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#eesult)
 - [Conclusion](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#conclusion)
 - [Project Reflection](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#project-reflection)
 - [Notebook](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#notebook)
 - [Reference](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#reference)


# Business Problem
According to [Statista](https://www.statista.com/statistics/457078/category-cart-abandonment-rate-worldwide/), websites that provide travel-related products have a 98% abandonment rate among all businesses. It can be associated with searching destinations, comparing accommodations and flight fares,  and complex buying processes within the customer journey. In addition, most travelers will not only visit one site; they visit an average of 38 websites before deciding where to book; that means the consumers spend more time searching for products, which will delay their buying decision cycle; and lead to low conversions and impact on sales.

# Soution
To help Swiss OTAs improve conversions across travelers' digital journeys, we designed a traveler insights dashboard that presents key metrics and growing trends by analyzing social media and search engine data, which can help OTAs to opt for booking expereince and content marketing

# Methods
We built a travel databased with data engeneer techniques, incldues
 - Data source: define data collection stratrgy by mapping out traveler's digital jounry
 - Data Architecture: define data structure and data flow
 - Data pipelines: construct data processing workflow include ETL and ELT 
 - Data Modelling: adapt ER model
 - Protoyping: visualize data in Tableau

<p align = "center">
<img width="893" alt="Data Architecture" src="https://user-images.githubusercontent.com/72688726/187533413-9f9aec3c-7b5d-441f-ba11-5c0e9aaa7494.png">
<br>Data Architecture
</p>
<br>

# Data Source
1. Instagram media data via [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/)
 - media post time
 - media type
 - caption
 - mentions
 - hashtags 
 - no. of likes, 
 - no. comments
2. Switzerland: [Switzerland Tourism | OpenData API](https://developer.myswitzerland.io)
 - destination identifier
 - attractions identifier
 - geopoint
  - longitude
  - latitude
3. Die Post: CSV
 - Postcode
 - Kantons and cities' names in English, German, and Franch
 - Short Code
 
# Result
**Business Questions 1**:
“How can we improve the tourist travel experience in Switzerland by utilizing social media and search engine data? “
1. What are the popular destinations in Switzerland that people search for traveling?
2. Which city do people are interested in the most in Switzerland?

**Business Questions 2**:
“How do individuals and businesses utilize social media hashtags to boost their online presence and performance?”
1. What are the popular hashtags (top 5) used in Switzerland?
2. What are the popular hashtags (top 5) based on Swiss canton, city, or destination names?

**Business Questions 3**:
“Is there any relation between the use of travel hashtags in social media and keywords search?”
Does google search influence people to use specific hashtags for their posts?
Hypothesis: The more google search in a particular location, the more the location hashtag will be used in the post.

<br>
<p align = "center">
<img width="838" alt="tags" src="https://user-images.githubusercontent.com/72688726/187530598-4457abd1-1ca8-452a-a5ec-129c52f2126b.png">
<br>Traveler Insight Dashboard Prototype
</p>
<br>

IG Hashtag Statistic gives information about the usage of hashtags in each Instagram post. Posts with the hashtag Zurich receives the most likes, which has 169’235 likes and 6’170 comments in Switzerland; in the same period, Valais and Luzern are the second and third place, with 144’957 and 120’267 likes. Then we look at the donut chart, Zurich Wallis and Uri are the most popular cantons, and Zurich, Zermatt, and Interlaken are the most admired cities. Therefore, we can conclude that Zurich is the most popular and most visited place in Switzerland.

## Prototype
A visual dashboard is created by using Tableau. It gives key metrics about travel destinations in Switzerland. 

The dashboard can be seen in 
[Tableau Public](https://public.tableau.com/app/profile/yang7231/viz/Dashboard_final_16402072757680/FinalDashboard?publish=yes)

# Conclusion
The design of the database helps us to realize the information that is obtained from both Google Trends and Instagram. We can generate insights to answer our business questions by establishing analysis requirements. Since we do not have data from the user side, the dashboard is more focused on the value creation to business providers such as online travel agents and marketing firms, so that can utilize matrics from this dashboard to provide more personalized service and products to travelers.

# Project Reflection
It was a great experience to apply my business and customer experience expertise to digital product design. From this course, I have learned many hard skills in the data engineering field; we had a chance to apply knowledge and utilize popular tools such as AWS and Airflow to realize our business idea within three months. Working on a big project within such a short time (while writing a master's thesis) was pretty stressful. Nevertheless, the gains of this module were tremendous.

# Notebook
  - Airflow Dag:
    - callapi.py: DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

  - Python & Jupyter Notebook:
    - List_of_Zip_code_Switzerland.ipynb: zip_code.csv data cleaning and loading to RDS_PostgreSQL
    - my_switzerland_API.ipynb: Fetching destination information with the use of MySwitzerland API
    - Insta_create_hashtag.ipynb: Fetching Instagram hashtag media information with the use of Instagram Graph API
