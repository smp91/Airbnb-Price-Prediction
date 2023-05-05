
# Forecasting Airbnb Prices using Machine Learning and Deep Learning Techniques

### A case study using data from the City of Montreal.

Montreal is one of the largest cities in Canada. It attracts thousands of tourists during the year. In this regard, Airbnb pricing is extremely important in a big city such as Montreal where there is a lot of competition. In this project we would try to identify the important features that properties should have or need to have in order to be in demand and also predict the appropriate price range for them so the host wouldn’t miss any potential income.


## Goals
1. What are the main feature that affect the price of a listing.
2. How much does the location and neighbourhood affect the price and the demand on a property?
3. Predicting the prices using Machine Learning and Deep Learning models.
## Data
The Data used for this project comes from a website named [Inside Airbnb](http://insideairbnb.com/).
As indicated in there website “Inside Airbnb is a mission driven project that provides data and
advocacy about Airbnb's impact on residential communities”. This website provides quarterly data
for the last 12 months from multiple cities around the world. It also provides a GeoJSON file of
neighbourhoods for each city.
Note: The data behind the Inside Airbnb site is sourced from publicly available information from the Airbnb site.
## Libraries

All necesary libraries are indicated at the beggining of the notebook. 
It is recommended to use <Anaconda> and <Jupyter Notebook>.
If you use Anaconda most of the packages used in this project are pre-installed.
The code should run with no issues using Python versions 3.*.
Some Libraries that may not be pre-installed:
GeoJason
geopandas
Folium
Scikit-Learn
XGBoost
Keras
Pickle

## Screenshots

![App Screenshot](https://github.com/smp91/CB-DS-Final_Project/blob/master/Screenshots/Screenshot%202022-10-25%20082243.jpg)

![App Screenshot](https://github.com/smp91/Airbnb-Price-Prediction/blob/master/Screenshots/Screenshot%202022-10-25%20173732.jpg)

![App Screenshot](https://github.com/smp91/CB-DS-Final_Project/blob/master/Screenshots/Screenshot%202022-10-25%20082405.jpg)

![App Screenshot](https://github.com/smp91/CB-DS-Final_Project/blob/master/Screenshots/Screenshot%202022-10-25%20082447.jpg)

![App Screenshot](https://github.com/smp91/CB-DS-Final_Project/blob/master/Screenshots/Screenshot%202022-10-25%20082549.jpg)

![App Screenshot](https://github.com/smp91/CB-DS-Final_Project/blob/master/Screenshots/Screenshot%202022-10-25%20082700.jpg)



## Conclusion
By comparing different models in which the lower the MSE and higher the R Squared, is the more accurate model, we can see that the Random Forest Regression and XGBoost Regression model showed the best results and predictions (these models were created for several different combinations of train-test-splits, in all different combinations Random Forest and XGBoost had the highest accuracy and showed extremely close results. However, in most cases the XGBoost model had a slightly more accurate prediction.

Our best performing model which was XGBoost was only able to explain nearly %50 of the variation in price. The remaning is probably made up of features that were not present in the data. I personally think that photos and reviews play a strong role in encouraging a guest to book a certain property and so can be expected to have a significant impact on price. 

Listnigs with a better photo quality and a better review sentiment may lead to a higher demand. Therefore, they could be priced at a higher rate.


- The number of people a property could host has the most significant impact on the perice of the listing.
- Unusual property types (ex. boats - all listed as 'other') have higher price.
- The number of bathrooms a property has could impact the price.
- Listing in this two specific neighbourhood in Montreal (Ville-marie & Plateau-Mont-Royal) have a higher average price.
- Ammenities such as: air conditioning, TV, internet, washer, dryer, iron are common among listings and have an positive impact on the price.
- Interestingly, non of the review score features are in the top feature that impact the price (This could be because most listings had a high review rate)
## Recommendations

- The prices on the data collected for this project were all the price of a listing on Airbnb website and not the actual price that any specific listing was rented to a traveller. If we had access to the actual price, it may could lead to more accurate results.
- Including a sentiment analysis of the reviews and adding it as a feature may have had some good impact on the model and is worth considering for futre work.
- Finding a way to incorporate the image quality as a feature in our model could be intereting.
- By removing some features that could not be known at the time a new property is going to be listed on the Airbnb website such as reviews and availability, maybe the model could be more helpful for a new host with no experience that wants to have estimation for a reasonable price for their property.