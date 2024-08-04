from pymongo import MongoClient

def connect_to_db(db_url:str)->MongoClient:
    return MongoClient(db_url)
