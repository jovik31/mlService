from pymongo import MongoClient
from dotenv import dotenv_values


class MongoConn():

    def __init__(self):

        env_vars = dotenv_values(".env")
        self.username = env_vars['MONGO_INITDB_ROOT_USERNAME']
        self.password = env_vars['MONGO_INITDB_ROOT_PASSWORD']
        self.database = env_vars['MONGO_INITDB_ROOT_DATABASE']
        self.connection = MongoClient()
