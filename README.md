<p align = "center">
<img width="700" src ="https://user-images.githubusercontent.com/72688726/187684537-4684634f-89e6-49a7-82b2-4b912576281a.jpeg">
</p>
<p align = "center">Photo by
<a href="https://user-images.githubusercontent.com/72688726/187684537-4684634f-89e6-49a7-82b2-4b912576281a.jpeg">Devam Jhabak</a> on <a href="https://unsplash.com/s/photos/spam?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</p>
<br>

# Discovering Immstagramable destinations in Switzerland
### A traveller insights analysis from data collection to data visualization

["Travel is complicated to book", Expedia(2015)](https://www.travelmarketreport.com/articles/Consumers-Visit-38-Sites-Before-Booking-Expedia-Says).
Indeed, booking a trip is far more complicated than we thought, the entire booking process includes searching destinations, and accommodation, checking flight fares and hotels price as well as comparing different products and packages, which makes the customer journey even more complicated than other industries. To help online travel agencies to improve conversation across travelers' digital journeys, we decided to build a travel data warehouse and create a data insight dashboard that helps Swiss OTAs optimize the online booking experience using social media and search engine data.  

# Authors & Contribution
 - [Carol Hsu](https://github.com/hsuwanying): Business Design, Data Strategy, Data Engeneering (Instagram, MySwtitzerland, Die Post), Data Analysis, Prototype
 - [Cheuh Yang](https://github.com/cyyang50): Data Architecture, Data Engeneering (Google Trend, Simplemap), Data Analysis, Prototype

# Project Requirements
  - To build an end-to-end data pipeline and make it available for business analysis in a data warehouse environment
  - Duration: Oct 01, 2021 ~ Dec 23, 2021
  - Use at least 2 APIs to obatian static and non static data
  - Present a prototype use data visualiation tools
 
# Table of Content
 - [Background](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#background)
 - [Business Problem](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#business-problem)
 - [Solution](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#solution)
 - [Methods](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#methods)
 - [Data Source](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#data-source)
 - [Result](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#result)
 - [Limitation](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#limitation)
 - [Conclusion](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#conclusion)
 - [Project Reflection](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#project-reflection)
 - [Code Files](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#code-files)
 - [Reference](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/README.md#reference)

# Background
> *Websites that provide travel-related products have a 98% abandonment rate among all businesses. Statista (2022)* 

According to Expedia(2015), travellers visit an average of [38 websites](https://advertising.expedia.com/blog/research/how-marketers-can-reach-travel-bookers-across-the-consumer-funnel/) before booking a trip. The booking process includes finding where to travel, which airline to fly with, where to stay, and so on. Each step involved too many products and options that put travelers in the paradox of choice and make the customer journey even more complicated than in other industries.

# Business Problem
Although online travel agencies still play an essential role in the early product search phase of a customer journey, with an increased researching and planning time, the less the OTAs can impact a traveler's buying decisions, that means, the more products or services a traveler views, the slow the person will make a purchase. The delayed traveler's buying decision cycle will eventually lead to low conversions and an impact on sales.

# Soution
When mapping out a traveler's digital journey, we found social media has gained importance in the traveler's decision-making process (Smith & Anderson,2018). Travel feeds on Instagram have become one of the powerful indicators that trigger travelers’ decision to plan where they should visit on upcoming trips (Han & Chen, 2021). To understand how social media and online search impact travelers' buying decisions and to help Swiss OTAs improve online booking experience and effective marketing, we designed a traveler insights dashboard that presents crucial metrics and trends by analyzing social media and search engine data.

# Methods
A travel database is built with the following data engeneer techniques: 
 1. Define Data Collection strategies: Define the scope of the project and collect data from accros traveler digital touchpoints
 2. Design Database and Construct Data Piplines: Present a business data schema Construct ETL and ELT workflow use [Apache Airflow](https://airflow.apache.org)
 3. Built Data Architecture: Demonstrates data system with [AWS RDS](https://aws.amazon.com/rds/) according to business needs
 4. Prototyping: Based on predefine business questions to design visualiation datashboard layout

<p align = "center">
<img width="600" alt="Data Architecture" src="https://user-images.githubusercontent.com/72688726/187533413-9f9aec3c-7b5d-441f-ba11-5c0e9aaa7494.png">
<br>Data Architecture
</p>
<br>

# Data Source
| Data Source                                                  | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/) | 1. **Need Facebook & Instagram Business accounts** (for an access token). <br />2. Access information to public account users such as @mention, #hashtag, metadata(no. of likes, comments) <br />3. Total requests **cannot exceed 200 times per hour per user**, with a maximum of 50 responses a page (25 responses for one API call).<br />4. A maximum of **30 unique hashtags** in a **7 days** timeframe |
| [MySwitzerland API](https://developer.myswitzerland.io)      | 1. A public API that provides swiss tourist content via MySwitzerland website. <br />2. Access information **name**, an **identifier** that refers to a unique ID of each **destination**, and corresponding **geo-location data**. <br />3. 4114 destinations stored in 412 pages<br />4. 1 request per second and 10 returns in a burst <br />5. Set `time. sleep(2)` to avoid blocking by the system |
| [die Post ](https://swisspost.opendatasoft.com/explore/dataset/plz_verzeichnis_v2/table/?disjunctive.postleitzahl) | Download the “PLZ_Verzeichnis” CSV file via the link<br />It provides  `Postleitzahl`, `Ortbez18`, and `Kanton`, and information of each city |

# Result: Proposed Prototype
We constructed data pipelines to address the business problem that presents critical metrics with our proposed traveler insight dashboard. The IG Hashtag Statistic graph gives information about hashtag usage in each Instagram post. We can answer the following questions:

<br>

**Business Questions 1**:
“How can we improve the tourist travel experience in Switzerland by utilizing social media and search engine data? “
1. What are the popular destinations in Switzerland that people search for traveling?
2. Which city do people are interested in the most in Switzerland?

**Business Questions 2**:
“How do individuals and businesses utilize social media hashtags to boost their online presence and performance?”
1. What are the popular hashtags (top 5) used in Switzerland?
2. What are the popular hashtags (top 5) based on Swiss canton, city, or destination names?

<br>
<p align = "center">
<img width="600" alt="IG Hashtag Statistic" src="https://user-images.githubusercontent.com/72688726/187530598-4457abd1-1ca8-452a-a5ec-129c52f2126b.png">
<br>IG Hashtag Statistic
</p>
<br>
Posts with the hashtag Zurich receives the most likes, which has 169’235 likes and 6’170 comments; in the same period, Valais and Luzern are the second and third popular place, with 144’957 and 120’267 likes respectively. Following that, the donut chart shows Zurich, Wallis and Uri are the most popular cantons, and Zurich, Zermatt, and Interlaken are the most admired cities. Therefore, we can conclude that Zurich is the most popular and most visited place in Switzerland.

A full dashboard can be seen in [Tableau Public](https://public.tableau.com/app/profile/yang7231/viz/Dashboard_final_16402072757680/FinalDashboard?publish=yes)


# Limitation
Ideally, we wanted to get location tags to create a traveler insights app, but Instagram depreciated local tag endpoints from its API due to privacy issues. There was no way to get location tags (I have also tried with web scraping but fail...). Therefore we decided to use #inLoveWithSwitzerland, the primary hashtag from MySwitzerland, and 26 Kanton names in English as the basis to fetch relevant tags in each Instagram post. Although we couldn't capture all the locations in Switzerland, the collected information was sufficient to create a minimal viable prototype for this project.

# Conclusion
The design of the database helps us to realize the information that is obtained from both Google Trends and Instagram. We can generate insights to answer our business questions by establishing analysis requirements. Since we do not have data from the user side, the dashboard is more focused on the value creation to business providers such as online travel agents and marketing firms, so that can utilize matrics from this dashboard to provide more personalized service and products to travelers.

# Project Reflection
This project taught me many hard skills in data engineering, which equipped me with fundamental skills and knowledge to interact with database tools and allowed me to combine design thinking with product development. Besides, having the opportunity to use popular software such as AWS and Airflow to realize our business idea into a monetizable product was an invaluable experience I had from this group work.

# Code Files
  - Airflow Dag:
    - [callapi.py](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/callapi.py): DAG file fetches media information from Posts on Instagram based on 30 unique hashtags

  - Jupyter Notebook:
    - [List_of_Zip_code_Switzerland.ipynb](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/List_of_Zip_code_Switzerland.ipynb): zip_code.csv data cleaning and loading to RDS_PostgreSQL
    - [my_switzerland_API.ipynb](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/my_switzerland_API.ipynb): Fetching destination information with the use of MySwitzerland API
    - [Insta_create_hashtag.ipynb](https://github.com/hsuwanying/traveller-insights-analysis/blob/main/Insta_create_hashtag.ipynb): Fetching Instagram hashtag media information with the use of Instagram Graph API
# Reference
 - [Expedia Group Media Solution (2015) *How Marketers Can Reach Travel Bookers Across the Consumer Funnel*](https://advertising.expedia.com/blog/research/how-marketers-can-reach-travel-bookers-across-the-consumer-funnel/) Retrieved on November 01, 2021
 - [Han, J & Chen, H. (2021) *Millennial Social media User’s Intention to Travel: The Moderating Role of Social Media Influencer Following Behavior*](https://www.emerald.com/insight/content/doi/10.1108/IHR-11-2020-0069/full/html) Retrieved on November 01, 2021
 - [Statista (2022) *Online Cart Abandonment Rate Worldwide*](https://www.statista.com/statistics/457078/category-cart-abandonment-rate-worldwide/)
 - [Smith A & Anderson M. (2018) *Social Media Use in 2018*](https://policycommons.net/artifacts/617452/social-media-use-in-2018/1598263/) Retrieved on October 11, 2021
