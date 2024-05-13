from fastapi import APIRouter
from router.supply_request_router import router as supply_request


router = APIRouter()

router.include_router(supply_request.router, tags=[
                      "suppley"], prefix="/request")
