# project description with goals

In this project we will be looking at a dataset of customer data from ficticious telecom company (Telco). We will attempt to predict the probablity that any given customer will churn (end their service subscriptions with Telco) based on factors such as monthly charges, billing type, gender and payment method. The data used in this project is static and will not be used for predictions on future customers.

There are a number of fields in our dataset which may have an effect upon customer churn rate which we will be unable to affect such as a customer's gender, dependents or age. These may be factors to consider for focusing marketing efforts in attracting new customers, but our focus will be on how to keep our existing customers from churning. Therefore we will be looking at services the company can provide or impove which may be a factor in customer churn rate.


# initial hypotheses and/or questions you have of the data, ideas

Do customers with both phone services and internet service churn less than average?
Do customers churn less with online security and online backup services than customers without?
Do customers with multiple phone lines churn less than customers with phone service on average?
Do customers with device protection and tech support churn less than customers without?
Does paperless billing have an effect on customer churn rate?
Do customers with streaming tv have a lower churn rate than those without?
Do customers with streaming movies have a lower churn rate than those without?
Do customers with both streaming tv and streaming movies churn at a lower rate than customers on average?
Is there a difference in churn among genders depending on if they have streaming tv or movie streaming?


# data dictionary
![alt text](https://github.com/Adam-Harris87/classification-project/blob/main/data_dictionary.png)


# project planning (lay out your process through the data science pipeline)

Planning - The project planning will be laid out in this readme

Acquisition - Data will be acquired via SQL function from the codeup server. Once the data is initially acquired, a telco.csv will be created in the user's local directory and reference instead of the SQL when accessed after the first time.

Preparation - The data will have duplicate columns due to joining tables in SQL, these will be removed. The total_charges column is imported with the incorrect data type, this will be changed to a float type. There are a number of columns with boolean style data that is currently stored as yes/no, these columns will be converted to 1/0. The data will then be encoded into one-hot-encoding and then split into train, validate, test sample sets in prepartation of using with machine learning algorithms.

Exploration - We will explore the data using various graphs, charts and visualizations in order to see if we can visually determine fields which will have a large impact upon predicting churn rate. We will then perform hypothesis testing in order to check if our visual determination of impactful fields is statistically accurate. We will finally choose a number of fields that have the most correlation to our churn target to use with our machine learning models.

Modeling - We will input our 4-5 most impactful fields into various machine learning algorlithms, and check the accuracy and recall scores of each model. We will consider a customer churn to be a positive condition of our prediction models. 
	
	Since we are looking to prevent customer churn we will be looking to predict as many true positive conditions as possible regardless of false positives, therefore we will be most concerned with the model's recall rate.

Delivery - Our delivery method will be an interactive Jupyter notebook containing methodology notes including useful exploration visualisations and recall score metrics from our highest performing models. There will also be a verbal presentation of the findings of this project.


# instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

In order to run the files in this project, the user will need to connect to the Codeup SQL database, in order to do this the user will need to have a file named 'env.py' in the same file directory as the project files. This env.py file will need to contain: 

user = 'your_username_to_connect_to_the_codeup_database'
password = 'your_password_for_the_codeup_database'
host = 'data.codeup.com'


# key findings, recommendations, and takeaways from your project.
