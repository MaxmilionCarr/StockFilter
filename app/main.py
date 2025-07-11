from fastapi import FastAPI
from app.routers import prices, news, alerts
import logging

app = FastAPI()

# Register Routers
app.include_router(prices.router)
app.include_router(news.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "Stock Alert API is Live"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

