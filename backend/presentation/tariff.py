from fastapi import APIRouter, Path
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from pydantic import BaseModel

from backend.infra.database import SqlTariffRepo
from backend.presentation.base import list_response
from backend.usecases.tariff import (
    CreateTariffCommand,
    CreateTariffDto,
    DeleteTariffCommand,
    UpdateTariffCommand,
    UpdateTariffDto,
)

router = APIRouter(route_class=DishkaRoute)


class CreateTariff(BaseModel):
    name: str
    descripiton: str
    price: int
    
    
@router.get("/")
async def tariff_list(repo: FromDishka[SqlTariffRepo]):
    items = await repo.get_all()
    return list_response(items)


@router.post("/")
async def tariff_post(tariff: CreateTariff, cmd: FromDishka[CreateTariffCommand]):
    result = await cmd(
        CreateTariffDto(
            name=tariff.name, descripiton=tariff.descripiton, price=tariff.price
        )
    )
    return result


@router.patch("/{id}")
async def tariff_update(
    update: CreateTariff,
    cmd: FromDishka[UpdateTariffCommand],
    id: str = Path(),
):
    return await cmd(UpdateTariffDto(id=id, **update.model_dump(exclude_unset=True)), update)


@router.delete("/{id}")
async def tariff_delete(
    cmd: FromDishka[DeleteTariffCommand],
    id: str = Path()
):
    return await cmd(id)
