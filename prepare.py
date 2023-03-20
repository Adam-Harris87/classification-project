# import libraries for working with arrays and DataFrames
import numpy as np
import pandas as pd
# import acquire library for retrieving telco data
import acquire
# import library to split our data for use with machine learning
from sklearn.model_selection import train_test_split

# Create a function named prep_telco that accepts the raw telco_df data,
# and returns the cleaned data
def prep_telco(telco_df):
    '''
    prep_telco will take in a DataFrame containing data from the Telco dataset.
    the function will drop columns 'payment_type_id', 'internet_service_type_id',
    'contract_type_id' because they are duplicate due to us joining tables via sql.
    The function will then convert 'total_charges' to float type.
    Then it will change columns containing only 'yes'/'no' values into 1/0 values
    and encore categorical columns to dummies then return the cleaned DataFrame.
    '''
    # Drop any unnecessary, unhelpful, or duplicated columns. 
    # 'payment_type_id', 'internet_service_type_id', 'contract_type_id' are redundant
    # since we joined tables in the sql query
    telco_df = telco_df.drop(columns=
                       ['payment_type_id',
                        'internet_service_type_id',
                        'contract_type_id'])
    
    # total_charges is showing up as an object type when it actually should be a float
    telco_df['total_charges'] = telco_df.total_charges.replace(
        ' ','').replace('','0').astype(float)
    
    # replace yes/no column values with 1/0
    telco_df['partner'] = telco_df.partner.map({'Yes': 1, 'No': 0})
    telco_df['dependents'] = telco_df.dependents.map({'Yes': 1, 'No': 0})
    telco_df['phone_service'] = telco_df.phone_service.map({'Yes': 1, 'No': 0})
    telco_df['paperless_billing'] = telco_df.paperless_billing.map({'Yes': 1, 'No': 0})
    telco_df['churn'] = telco_df.churn.map({'Yes': 1, 'No': 0})
    
    # convert the categorical data into dummies
    telco_df = pd.concat(
        [telco_df, pd.get_dummies(telco_df[[
         'gender',
         'multiple_lines',
         'online_security',
         'online_backup',
         'device_protection',
         'tech_support',
         'streaming_tv',
         'streaming_movies',
         'contract_type',
         'internet_service_type',
         'payment_type'
        ]], drop_first=True)],
                      axis=1)
    
    # now we have column names with spaces, which we don't want
    # let's rename the columns with spaces, remove ()s and lower case everything
    new_names = []
    for col in telco_df.columns.to_list():
        new_names.append(col.replace(' ', '_').replace('(','').replace(')', '').lower())
    telco_df.columns = new_names
    

    # create a column identifying customers with neither online security or
    # online backup services
    telco_df['neither_security_or_backup'] = ((telco_df.online_backup == 'No') 
                                   & (telco_df.online_security == 'No'))

    # return the clean DataFrame
    return telco_df

def split_data(df, random_seed=4233):
    '''
    split_data will take in a DataFrame and a stratify target (default to 'churn')
    random_seed is also asignable (default = 4233 for no reason).
    It will return the data split up for ML models. 
    The return values are: train, validate, test
    '''
    
    # split our df into train_val and test:
    train_val, test = train_test_split(df,
                                       train_size=0.8,
                                       random_state=random_seed,
                                       stratify=df['churn'])
    
    # split our train_val into train and validate:
    train, validate = train_test_split(train_val,
                                       train_size=0.7,
                                       random_state=random_seed,
                                       stratify=train_val['churn'])
    # return the split DataFrames
    return train, validate, test

def wrangle():
    '''
    The wrangle function will retreive a DataFrame containing the telco dataset
    by using the get_telco_data contained in the acquire.py file.
    The function will then clean the data using the prep_telco function, and then
    split the cleaned data and return the data as DataFrames:
    train, validate, test 
    '''
    # retrieve telco data, and clean the data
    telco = prep_telco(acquire.get_telco_data())
    # # split the data for use in machine learning models
    # train, validate, test = split_data(telco)
    # # return the split DataFrames
    # return train, validate, test
    return telco