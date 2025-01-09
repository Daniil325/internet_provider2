from dataclasses import dataclass
from uuid import UUID
from fastapi import HTTPException, status

from backend.core.entities import Client
from backend.infra.auth import authenticate_client, create_access_token, get_password_hash
from backend.infra.database import SqlClientRepo


@dataclass
class CreateClientDto:
    fio: str
    phone: str
    email: str
    username: str
    password: str


@dataclass
class CreateClientCommand:
    repo: SqlClientRepo

    async def __call__(self, dto: CreateClientDto) -> str | None:
        client = await self.repo.get_by_email(dto.email)
        if client:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Пользователь уже существует",
            )
        identity = self.repo.new_id()
        password = get_password_hash(dto.password)
        client = Client(identity, dto.fio, dto.phone, dto.email, dto.username, password)
        await self.repo.add(client)
        return identity
    

@dataclass
class LoginClientDto:
    email: str
    password: str
    

@dataclass
class LoginClientCommand:
    repo: SqlClientRepo
    
    async def __call__(self, dto: LoginClientDto, password: str):
        client = await self.repo.get_by_email(dto.email)
        check = await authenticate_client(client, password)
        if check is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
        access_token = create_access_token({"sub": str(check.id)})
        return access_token
