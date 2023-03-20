# import libraries for working with arrays and DataFrames
import numpy as np
import pandas as pd
# import data visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# import functions for retrieving and cleaning telco dataset
import prepare

# retrieve data from sql database, and clean the data
df = prepare.wrangle()
# split data into train, validate, test groups
train, validate, test = prepare.split_data(df)

def get_pie_total():
    '''This function will display a pie chart of the total customer churn rate'''
    # create the pie chart
    plt.pie(train.churn.value_counts(), labels=("Didn't churn",'Churned'), 
            autopct='%1.1f%%', colors=('cornflowerblue', 'red'), startangle=90)
    # give the pie chart a title
    plt.title('About 26.5% of Customers Will Churn')
    # display the pie chart
    plt.show()

# Do customers with both phone services and internet service churn less than 
# customers that only have one service?

# create a variable to group customers with both service types
train['phone_and_internet'] = ((train.phone_service == 1) 
                               & (train.internet_service_type_none == 0))

def get_bar_phone_and_internet():
    '''
    This function will display a barplot of customer churn rates for customers
    who have one service type and customers who have both service types.
    '''
    # create the bar plot
    sns.barplot(data=train,
               x='phone_and_internet',
               y='churn')
    # change the tick labels to something understandable
    plt.xticks(ticks=(False, True), labels=('One Service','Phone & Internet'))
    # add axis labels
    plt.xlabel('Customer Service Subscriptions')
    plt.ylabel('Customer Churn Rate')
    # add a chart title
    plt.title('Customers With Both Phone and Internet Services Have a \n\
    Higher Churn Rate Than Customers With Only One Service Type')
    # add a line showing the average churn rate
    plt.axhline(train.churn.mean(), ls='--', color='black', label='Average Churn')
    # create a legend to describe the avg churn rate line
    plt.legend()
    # show the chart
    plt.show()
    