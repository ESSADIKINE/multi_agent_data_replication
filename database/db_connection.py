from pymongo import MongoClient
from config.settings import MONGO_HOST, MONGO_PORT

class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
    
    def get_database(self, db_name):
        return self.client[db_name]
    
    def get_collection(self, db_name, collection_name):
        db = self.get_database(db_name)
        return db[collection_name]
