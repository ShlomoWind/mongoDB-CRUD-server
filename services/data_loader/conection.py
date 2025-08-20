import os
from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.db_name = os.getenv("MONGO_DB_NAME", "my_database")
        self.collection_name = os.getenv("MONGO_COLLECTION_NAME", "my_collection")
        self.mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]