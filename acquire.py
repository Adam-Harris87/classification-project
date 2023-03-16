# import libraries to work with arrays and DataFrames
import numpy as np
import pandas as pd
# import libraries to importing data from sql and/or csv
import os
import env

# function to create a sql connection string
def get_db_url(db_name, host=env.host, user=env.user, password=env.password):
    '''
    The get_db_url function will return a sql connection url string.
    This function relies on there being an env.py file in the local directory containing:
    host (sql database host address), 
    user (username to connect to sql database), 
    password (password for your username to connect to the sql database)
    '''
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url

# function to retrieve the telco dataset
def get_telco_data():
    '''
    get_telco_data will look for a telco.csv file in the local directory, 
    if one does not exist, the function will connect to a sql database utilizing
    the get_db_url and retrieve the telco_churn data then create a telco.csv file
    and return the data as a pandas DataFrame
    otherwise, if the file exists this function will open the telco.csv file
    and return the data as a pandas DataFrame.
    '''
    
    filename = "telco.csv"

    #check if cached exists
    if os.path.isfile(filename):
        #return cached data
        print('opening data from file')
        return pd.read_csv(filename, index_col=0)
    else:
        # read the SQL query into a dataframe
        print('cached file not found, creating new file')
        # create connection string using get_db_url function
        connection = get_db_url('telco_churn')
        # sql query
        query = '''
SELECT *
FROM customers
	JOIN contract_types
		USING (contract_type_id)
	JOIN internet_service_types
		USING (internet_service_type_id)
	JOIN payment_types
		USING (payment_type_id)
-- limit 5
;
        '''
        df = pd.read_sql(query, connection)
    
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)
        # return the dataframe
        return df