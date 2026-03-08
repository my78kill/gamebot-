from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["battle_game"]

users = db["users"]
blocked = db["blocked"]