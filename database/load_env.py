import os
from dotenv import dotenv_values


def load_postgres_environment_variables():
    '''
    load_dotenv()
    db = os.getenv('POSTGRES_DB')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    root_password = os.getenv
    '''

    return dotenv_values(".env")


config = load_postgres_environment_variables()

print(config)
