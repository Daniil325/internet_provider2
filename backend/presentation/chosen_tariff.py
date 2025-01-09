from uuid import UUID
from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from pydantic import BaseModel

from backend.infra.database import SqlChosenTariffRepo
from backend.presentation.base import list_response
from backend.usecases.chosen_tariff import CreateChosenTariffCommand, CreateChosenTariffDto


router = APIRouter(route_class=DishkaRoute)


class CreateChosenTariff(BaseModel):
    client_id: UUID
    tariff_id: UUID
    
    
@router.get("/")
async def chosen_tariffs_list(repo: FromDishka[SqlChosenTariffRepo]):
    items = await repo.get_all()
    return list_response(items)


@router.post("/")
async def chosen_tariff_create(chosen_tariff: CreateChosenTariff, cmd: FromDishka[CreateChosenTariffCommand]):
    result = await cmd(
        CreateChosenTariffDto(
            client_id=chosen_tariff.client_id, tariff_id=chosen_tariff.tariff_id
        )
    )
    return result