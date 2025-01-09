from fastapi import APIRouter

from .client import router as client_router
from .tariff import router as tariff_router
from .payment import router as payment_router
from .chosen_tariff import router as chosen_tariff_router

api_router = APIRouter()
api_router.include_router(client_router, prefix="/client", tags=["client"])
api_router.include_router(tariff_router, prefix="/tariff", tags=["tariff"])
api_router.include_router(payment_router, prefix="/payment", tags=["payment"])
api_router.include_router(
    chosen_tariff_router, prefix="/chosen_tariff", tags=["chosen_tariff"]
)
