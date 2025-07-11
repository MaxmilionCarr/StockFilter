import asyncio
from app.database import SessionLocal
from app.models.stock import Stock
from app.config import settings

async def seed_stocks():
    async with SessionLocal() as session:
        for ticker in settings.TRACKED_TICKERS:
            stock = Stock(
                ticker=ticker,
                name=f"{ticker} Inc.",
                sector="Technology",
                industry="Software"
            )
            session.add(stock)
        await session.commit()
        print("Seeded stocks:", settings.TRACKED_TICKERS)

if __name__ == "__main__":
    asyncio.run(seed_stocks())
