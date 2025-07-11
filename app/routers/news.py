from fastapi import APIRouter

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/ping")
async def ping_news():
    return {"message": "News router is live"}