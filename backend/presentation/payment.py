from uuid import UUID
from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from pydantic import BaseModel

from backend.infra.database import SqlPaymentRepo
from backend.presentation.base import list_response
from backend.usecases.payment import CreatePaymentCommand, CreatePaymentDto


router = APIRouter(route_class=DishkaRoute)


class CreatePayment(BaseModel):
    client_id: UUID
    amount: int


@router.get("/")
async def payments_list(repo: FromDishka[SqlPaymentRepo]):
    items = await repo.get_all()
    return list_response(items)


@router.post("/")
async def payment_create(payment: CreatePayment, cmd: FromDishka[CreatePaymentCommand]):
    result = await cmd(
        CreatePaymentDto(client_id=payment.client_id, amount=payment.amount)
    )
    return result
