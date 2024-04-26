from pymongo import MongoClient
from models.connection.mongo_db_credentials import *

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'mongodb://{}:{}@{}:{}'.format(
            MONGO_USER,
            MONGO_PASSWORD,
            MONGO_HOST,
            MONGO_PORT
        )
        self.__db_name = MONGO_DB_NAME
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__db_name]

    def get_db_connection(self):
        return self.__db_connection
        