from fastapi import APIRouter, Response
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from pydantic import BaseModel

from backend.infra.database import SqlClientRepo
from backend.presentation.base import list_response
from backend.usecases.client import (
    CreateClientCommand,
    CreateClientDto,
    LoginClientCommand,
)


router = APIRouter(route_class=DishkaRoute)


class CreateClient(BaseModel):
    fio: str
    phone: str
    email: str
    username: str
    password: str


@router.get("/")
async def client_list(repo: FromDishka[SqlClientRepo]):
    items = await repo.get_all()
    return list_response(items)


@router.post("/register")
async def register_client(client: CreateClient, cmd: FromDishka[CreateClientCommand]):
    result = await cmd(
        CreateClientDto(
            fio=client.fio,
            phone=client.phone,
            email=client.email,
            username=client.username,
            password=client.password,
        )
    )
    return result


class LoginClient(BaseModel):
    email: str
    password: str


@router.post("/login")
async def login_client(
    response: Response, client: LoginClient, cmd: FromDishka[LoginClientCommand]
):
    result = await cmd(
        LoginClient(
            email=client.email,
            password=client.password,
        ),
        client.password,
    )
    response.set_cookie(key="users_access_token", value=result, httponly=True)
    return {"access_token": result, "refresh_token": None}
