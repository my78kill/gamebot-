from pymongo import MongoClient
from config import MONGO_URI
import certifi

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["battle_game"]

users = db["users"]
blocked = db["blocked"]
