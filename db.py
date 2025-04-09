import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

MONGO_URL = os.getenv("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["portfolio_db"]  # database name
