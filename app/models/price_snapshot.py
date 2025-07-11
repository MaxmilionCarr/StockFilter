from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class PriceSnapShot(Base):
    __tablename__ = "price_snapshots"

    id = Column(String, primary_key=True)
    ticker = Column(String, ForeignKey("stocks.ticker"))
    timestamp = Column(DateTime, default=datetime.now())
    price = Column(Float)