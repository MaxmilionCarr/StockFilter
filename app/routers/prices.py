from fastapi import APIRouter
from sqlalchemy import select, desc
from app.models.price_snapshot import PriceSnapShot
from app.database import SessionLocal
from app.config import settings
from app.services.prices import fetch_price_data, store_prices

router = APIRouter(prefix="/prices", tags=["Price"])

@router.get("/ping")
async def ping_prices():
    return {"message": "Price router is live"}


@router.get("/latest")
async def latest_prices():
    return await fetch_price_data()

@router.post("/update")
async def update_prices():
    prices = await fetch_price_data()
    await store_prices(prices)
    return {"status": "stored", "data": prices}

@router.get("/latest")
async def get_latest_prices():
    async with SessionLocal() as session:
        prices = {}
        for ticker in settings.TRACKED_TICKERS:
            stmt = (
                select(PriceSnapShot)
                .where(PriceSnapShot.ticker == ticker)
                .order_by(desc(PriceSnapShot.timestamp))
                .limit(1)
            )
            result = await session.execute(stmt)
            latest = result.scalar_one_or_none()
            prices[ticker] = latest.price if latest else None
        return prices
        