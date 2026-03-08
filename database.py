from pymongo import MongoClient
from config import MONGO_URI
import certifi

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

# Database
db = client["battle_game"]

# Collections
users = db["users"]
blocked = db["blocked"]

# Optional indexes (performance better)
users.create_index("id", unique=True)
blocked.create_index("id", unique=True)
