from fastapi import APIRouter
from app.services import prices, news, alerts

router = APIRouter(prefix="/prices", tags=["Price"])

@router.get("/ping")
async def ping_prices():
    return {"message": "Price router is live"}


@router.get("/latest")
async def latest_prices():
    return await prices.fetch_price_data()