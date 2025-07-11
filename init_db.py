import asyncio
from app.database import engine, Base
from app.models.stock import Stock
from app.models.price_snapshot import PriceSnapshot

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())

    import sqlite3
    conn = sqlite3.connect("stock_alert.db")
    print(conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
    import os
    print("CREATING DB FILE AT:", os.path.abspath("stock_alert.db"))

