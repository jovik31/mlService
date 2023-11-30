import psycopg2
import pymongo
import os
from dotenv import load_dotenv


load_dotenv()

var = os.getenv('POSTGRES_DB')
print(var)
