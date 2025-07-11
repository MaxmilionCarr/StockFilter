import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_URL = os.getenv("DB_URL", "sqlite+aiosqlite:///./stock_alert.db")
    STOCK_API_KEY = os.getenv("STOCK_APIT_KEY", "demo")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    TRACKED_TICKERS = ["AAPL", "TSLA", "GOOGL", "NVDA"]

settings = Settings()