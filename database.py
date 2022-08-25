import psycopg2
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

class Database:
    pass
    # def __init__(self):
    #     self.connection = psycopg2.connect(
    #     database = os.environ.get('DATABASE', config["DATABASE"]), 
    #     user = os.environ.get('USER', config["USER"]),
    #     password = os.environ.get('PASSWORD', config["PASSWORD"]), 
    #     host = os.environ.get('HOST', config["HOST"]), 
    #     port = int(os.environ.get('PORT', config["PORT"]))
    #     )
    #     self.cursor = self.connection.cursor()

    
