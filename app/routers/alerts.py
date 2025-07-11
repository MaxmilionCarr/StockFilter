from fastapi import APIRouter

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/ping")
async def ping_alerts():
    return {"message": "Alert router is live"}