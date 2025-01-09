from typing import Generic, Type, TypeVar
from uuid import UUID
import uuid
from dataclasses import asdict

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from backend.infra.session import PostgresSession
from backend.core.entities import ChosenTariff, Client, Payment, Tariff
from backend.core.protocols import ChosenTariffRepo, ClientRepo, PaymentRepo, TariffRepo

T = TypeVar("T")


class SqlHelper(Generic[T]):

    def __init__(self, session: AsyncSession, model: Type[T]) -> None:
        self._session = session
        self._model = model
        
    @staticmethod
    def new_id() -> str:
        return uuid.uuid4()

    async def get_all(self) -> list[T]:
        stmt = select(self._model)
        return (await self._session.execute(stmt)).scalars().all()

    async def get_by_id(self, id: UUID):
        stmt = select(self._model).where(self._model.id == id)
        return (await self._session.execute(stmt)).scalar_one_or_none()

    async def add(self, obj):
        self._session.add(obj)
        await self._session.commit()

    async def update(self, id: UUID, obj):
        print("hhhhhh", type(obj))
        stmt = update(self._model).where(self._model.id == id).values(obj.dict())
        await self._session.execute(stmt)
        await self._session.commit()

    async def delete(self, id: UUID):
        stmt = delete(self._model).where(self._model.id == id)
        await self._session.execute(stmt)
        await self._session.commit()


class SqlTariffRepo(SqlHelper, TariffRepo):

    def __init__(self, session):
        super().__init__(session, Tariff)


class SqlClientRepo(SqlHelper, ClientRepo):

    def __init__(self, session):
        super().__init__(session, Client)
        
    async def get_by_email(self, email: str) -> Client | None:
        stmt = select(Client).where(Client.email == email)
        return (await self._session.execute(stmt)).scalar_one_or_none()


class SqlChosenTariffRepo(SqlHelper, ChosenTariffRepo):

    def __init__(self, session):
        super().__init__(session, ChosenTariff)


class SqlPaymentRepo(SqlHelper, PaymentRepo):

    def __init__(self, session):
        super().__init__(session, Payment)
