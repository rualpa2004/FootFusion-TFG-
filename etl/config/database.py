from pymongo import MongoClient
from settings import MONGODB_URI, MONGODB_DB_NAME

_client = None
_db = None

def get_database():
    global _client, _db
    if _db is None:
        _client = MongoClient(MONGODB_URI)
        _db = _client[MONGODB_DB_NAME]
    return _db