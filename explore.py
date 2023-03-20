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
               y='churn',
               ci=False)
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

def get_bar_security_or_backup():
    ''' 
    This function will display a bar plot showing the churn rate of customers 
    who have security or backup services and customers who have neither service
    '''
    # create a bar plot
    sns.barplot(data=train,
                x='neither_security_or_backup',
                y='churn',
                ci=False)
    # create a line showing the total average churn rate
    plt.axhline(train.churn.mean(), ls='--', color='black', label='Total Average Churn')
    # display a legend describing the average churn line
    plt.legend()
    # change the axis labels
    plt.ylabel('Customer Churn Rate')
    plt.xlabel('Security or Backup Subscription')
    # change the description for each bar
    plt.xticks(ticks=(False, True), labels=('Has At Least One Service',
                                            'Has Neither Service'))
    # add a title for the chart
    plt.title('Customers With Neither Internet Security or Online Backup Services\n\
    Have a Higher Churn Rate Than Customers With At Least One Service')
    plt.show()

def get_ttest_neither_security_or_backup():
    '''
    This function will perform a t-test on the sample of customers who do not have either
    online security or backup services, compared to the churn rate of all customers
    '''
    # set the alpha score
    alpha = 0.05
    # get the churn rate of customer subset that we are looking at
    nsob_churn = train[train['neither_security_or_backup']].churn
    # run the t-test on our sample compared to the total churn rate
    t_stat, p = stats.ttest_ind(nsob_churn, 
                                train.churn, equal_var=False)
    # a t-stat > 0 and p / 2 < alpha will indicate that having neither security
    # or backup services has a higher churn rate than customers with at least one service
    print(f'T_stat is greater than 0: {t_stat > 0}, T_stat = {t_stat:.6}')
    print(f'p-value / 2 is less than alpha: {p / 2 < alpha}, p-value / 2 = {p/2:.6}')

def get_bar_tech_support():
    '''
    This function will display a bar graph of the churn rate of customers who have tech
    support service and customers who do not.
    '''
    # create the bar chart
    sns.barplot(data=train,
                x='tech_support_yes',
                y='churn',
                ci=False)
    # change the xtick labels to understandable text
    plt.xticks(ticks=(0,1), labels=('No Tech Support', 'Has Tech Support'))
    # create x and y axis labels
    plt.xlabel('Customers With or Without Tech Support')
    plt.ylabel('Customer Churn Rate')
    # create a chart title
    plt.title('Customers With Tech Support Have a Lower Churn Rate\n\
    Than Customers Without Tech Support')
    # create a line showing the overall average churn rate
    plt.axhline(train.churn.mean(), ls='--', color='black', label='Total Average Churn')
    # add a legend describing the average churn rate line
    plt.legend()
    # show the chart
    plt.show()

def get_ttest_tech_support():
    '''
    This function will perform a t-test on the sample of customers who have tech support
    compared to the churn rate of all customers.
    '''
    # set the alpha score
    alpha = 0.05
    # get the churn rate of customer subset that we are looking at
    tech_churn = train[train['tech_support_yes'] == 1].churn
    # run the t-test on our sample compared to the total churn rate
    t_stat, p = stats.ttest_ind(tech_churn, 
                                train.churn, equal_var=False)
    # a t-stat < 0 and p / 2 < alpha will indicate that customers with tech support service
    # have a lower churn rate than customers without it
    print(f'T_stat is less than 0: {t_stat < 0}, T_stat = {t_stat:.6}')
    print(f'p-value / 2 is less than alpha: {p / 2 < alpha}, p-value / 2 = {p/2:.6}')

def get_bar_dependents():
    '''
    This function will display a visualization for customer churn rate based on if
    the customer has dependents or not.
    '''
    # Does a customer having dependents change the rate of customer churn?
    # create the bar graph
    sns.barplot(data=train,
                x='dependents',
                y='churn',
                ci=False)
    # change the xticks to something understandable
    plt.xticks(ticks=(0,1), labels=('No Dependents', 'Has Dependents'))
    # change the axis labels
    plt.xlabel('Customer Dependents')
    plt.ylabel('Customer Churn Rate')
    # create a title for the graph
    plt.title('Customers With Dependents Have a Lower Churn Rate')
    # create a line showing the total average churn rate
    plt.axhline(train.churn.mean(), ls='--', color='black', label='Total Average Churn')
    # create a legend explaining the avg churn rate line
    plt.legend()
    # show the graph
    plt.show()

