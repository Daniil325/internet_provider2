from sqlalchemy import Column, ForeignKey, Integer, String, Table, Uuid
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from backend.infra.session import build_url
from backend.settings import Settings
from backend.core.entities import ChosenTariff, Client, Payment, Tariff

mapper_reg = registry()
metadata = mapper_reg.metadata


class SqlAlchemyDB:

    def __init__(self):
        config = Settings()
        dsn = build_url(
            config.POSTGRES_USER,
            config.POSTGRES_PASSWORD,
            config.POSTGRES_HOST,
            config.POSTGRES_PORT,
            config.POSTGRES_DB,
        )
        self.engine = create_async_engine(
            dsn, echo=False, pool_pre_ping=True, pool_recycle=3600
        )

        self.sessionmaker = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    async def close(self):
        await self.engine.dispose()


tariff_table = Table(
    "tariff",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("name", String, nullable=False),
    Column("descripiton", String, nullable=False),
    Column("price", Integer, nullable=False),
)

client_table = Table(
    "client",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("fio", String, nullable=False),
    Column("phone", String, nullable=False),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
)

chosen_tariff_table = Table(
    "chosen_tariff",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("client_id", Uuid, ForeignKey("client.id"), nullable=False),
    Column("tariff_id", Uuid, ForeignKey("tariff.id"), nullable=False),
)

payment_table = Table(
    "payment",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("client_id", Uuid, ForeignKey("client.id"), primary_key=True),
    Column("amount", Integer, primary_key=True),
)

mapper_reg.map_imperatively(Tariff, tariff_table)
mapper_reg.map_imperatively(Client, client_table)
mapper_reg.map_imperatively(ChosenTariff, chosen_tariff_table)
mapper_reg.map_imperatively(Payment, payment_table)
