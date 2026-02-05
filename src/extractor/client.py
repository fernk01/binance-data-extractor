import os
from dotenv import load_dotenv
from binance.spot import Spot

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

if not api_key or not api_secret:
    raise RuntimeError("API keys are not set in environment variables")

client = Spot(api_key, api_secret)
