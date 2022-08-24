import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
        database='d9gqvs86n94qnb', 
        user='gyjskygaxyvkqw',
        password='445ec1a2a4b07f2a769464d1a7945195ac09e214f0b463b47e55fdbc7de1f840', 
        host='ec2-34-248-169-69.eu-west-1.compute.amazonaws.com', 
        port=5432)
        self.cursor = self.connection.cursor()

    
