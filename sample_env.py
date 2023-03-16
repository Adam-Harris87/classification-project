user = 'your_username_for_sql_server'
password = 'your_password_for_sql_server'
host = 'data.codeup.com'

def get_db_url(db_name, host=host, user=user, password=password):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url