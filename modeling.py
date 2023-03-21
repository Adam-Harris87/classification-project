import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix, recall_score,\
accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# create a list of columns to be used as the ML model parameters 
X_cols = ['multiple_lines_no_phone_service', 'dependents',
           'multiple_lines_yes', 'online_security_yes',
           'online_backup_yes', 'device_protection_yes', 
           'tech_support_yes', 'contract_type_one_year',
           'contract_type_two_year', 'internet_service_type_fiber_optic',
           'internet_service_type_none', 'payment_type_credit_card_automatic',
           'payment_type_electronic_check', 'payment_type_mailed_check']
# create a variable for the column used as the prediction target of the ML models
y_col = 'churn'

def model_prep(train, validate, test):
    '''
    This function will take in train, validate and test DataFrames and return 
    DataFrames that contain the columns to be used with the ML models.
    '''
    # create new dataframes with the desired columns
    train_X = train[X_cols]
    validate_X = validate[X_cols]
    test_X = test[X_cols]
    train_y = train[y_col]
    validate_y = validate[y_col]
    test_y = test[y_col]
    # return the new dataframes
    return train_X, validate_X, test_X, train_y, validate_y, test_y

def get_decision_tree(train_X, validate_X, train_y, validate_y):
    '''
    This function will use a decision tree machine learning model to predict 
    customer churn using the columns chosen during the exploration process.
    '''
    # make the decision tree object
    dt = DecisionTreeClassifier()
    # fit the data to the dt object
    dt.fit(train_X, train_y)
    # predict with the dt object
    dt_preds = dt.predict(train_X)
    dt_val_preds = dt.predict(validate_X)
    # "Model Type" 
    # "evaluation metric" on train: "evaluation result" 
    # "evaluation metric" on validate: "evaluation result"
    print('Decision Tree Model')
    print(f'Recall score on train: {recall_score(train_y, dt_preds):.2%}')
    print(f'Recall score on validate: {recall_score(validate_y, dt_val_preds):.2%}')
    # return the decision tree model for use in other functions
    return dt

def get_random_forest(train_X, validate_X, train_y, validate_y):
    '''
    This function will use a random forest machine learning model to predict 
    customer churn using the columns chosen during the exploration process.
    '''
    # make the decision tree object
    rf = RandomForestClassifier()
    # fit the data to the rf object
    rf.fit(train_X, train_y)
    # predict with the rf object
    rf_preds = rf.predict(train_X)
    rf_val_preds = rf.predict(validate_X)
    # "Model Type" 
    # "evaluation metric" on train: "evaluation result" 
    # "evaluation metric" on validate: "evaluation result"
    print('Random Forest Model')
    print(f'Recall score on train: {recall_score(train_y, rf_preds):.2%}')
    print(f'Recall score on validate: {recall_score(validate_y, rf_val_preds):.2%}')
    # return the random forest model for use in other functions
    return rf

def get_logistic_regression(train_X, validate_X, train_y, validate_y):
    '''
    This function will use a logistic regression machine learning model to predict 
    customer churn using the columns chosen during the exploration process.
    '''
    # make the decision tree object
    lr = RandomForestClassifier()
    # fit the data to the lr object
    lr.fit(train_X, train_y)
    # predict with the lr object
    lr_preds = lr.predict(train_X)
    lr_val_preds = lr.predict(validate_X)
    # "Model Type" 
    # "evaluation metric" on train: "evaluation result" 
    # "evaluation metric" on validate: "evaluation result"
    print('Logistic Regression Model')
    print(f'Recall score on train: {recall_score(train_y, lr_preds):.2%}')
    print(f'Recall score on validate: {recall_score(validate_y, lr_val_preds):.2%}')
    # return the logistic regression model for use in other functions
    return lr

def get_rf_test(test_X, test_y, rf):
    '''
    This function will take in a random forest model in order to predict customer
    churn rate using the test data.
    '''
    # make a prediction using the test data and passed rf model
    rf_test_preds = rf.predict(test_X)
    # print the recall score for the test data
    print('Random Forest Model')
    print(f'Recall score on test: {recall_score(test_y, rf_test_preds):.2%}')