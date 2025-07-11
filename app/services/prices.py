import uuid
import yfinance as yf
from app.config import settings
from datetime import datetime
from sqlalchemy import insert
from app.database import SessionLocal
from app.models.price_snapshot import PriceSnapShot

async def fetch_price_data():
    tickers = settings.TRACKED_TICKERS
    data = yf.download(tickers=tickers, period="1d", interval="1m", progress=False, threads=False)

    prices = {}
    if isinstance(data["Close"], float):  # single ticker fallback
        prices[tickers[0]] = data["Close"]
    else:
        for ticker in tickers:
            try:
                prices[ticker] = round(data["Close"][ticker].dropna().iloc[-1], 2)
            except Exception:
                prices[ticker] = None
    return prices

async def store_prices(prices: dict):
    async with SessionLocal() as session:
        for ticker, price in prices.items():
            if price is None:
                continue
            
            snapshot = PriceSnapShot(
                id=str(uuid.uuid4()),
                ticker=ticker,
                timestamp=datetime.now(),
                price=price
            )
            session.add(snapshot)
        await session.commit()
