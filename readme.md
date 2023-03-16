# project description with goals

In this project we will be looking at a dataset of customer data from ficticious telecom company (Telco). We will attempt to predict the probablity that any given customer will churn (end their service subscriptions with Telco) based on factors such as monthly charges, billing type, gender and payment method. The data used in this project is static and will not be used for predictions on future customers.


# initial hypotheses and/or questions you have of the data, ideas


# data dictionary
![alt text](https://github.com/Adam-Harris87/classification-project/blob/main/data_dictionary.png)


# project planning (lay out your process through the data science pipeline)
Planning - The project planning will be laid out in this readme

Acquisition - Data will be acquired via SQL function from the codeup server. Once the data is initially acquired, a telco.csv will be created in the user's local directory and reference instead of the SQL when accessed after the first time.

Preparation - The data will have duplicate columns due to joining tables in SQL, these will be removed. The total_charges column is imported with the incorrect data type, this will be changed to a float type. There are a number of columns with boolean style data that is currently stored as yes/no, these columns will be converted to 1/0. The data will then be encoded into one-hot-encoding and then split into train, validate, test sample sets in prepartation of using with machine learning algorithms.

Exploration - We will explore the data using various graphs, charts and visualizations in order to see if we can visually determine fields which will have a large impact upon predicting churn rate. We will then perform hypothesis testing in order to check if our visual determination of impactful fields is statistically accurate. We will finally choose a number of fields that have the most correlation to our churn target to use with our machine learning models.

Modeling
Delivery

# instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)


# key findings, recommendations, and takeaways from your project.
