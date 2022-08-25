import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
        database = config["DATABASE"], 
        user = config["USER"],
        password = config["PASSWORD"], 
        host = config["HOST"], 
        port = int(config["PORT"]))
        self.cursor = self.connection.cursor()

    
