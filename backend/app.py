from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.infra.di import SqlProvider
from backend.infra.mapping import SqlAlchemyDB
from backend.usecases import CommandsProvider
from backend.presentation import api_router


def build_container():
    db = SqlAlchemyDB()
    return make_async_container(db.sessionmaker)


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = await build_container()
    app.state.container = container
    yield
    await app.state.dishka_container.close()


def create_app():
    app: FastAPI = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:3000'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router)
    app.state.db = SqlAlchemyDB()
    container = make_async_container(
        SqlProvider(app.state.db.sessionmaker),
        CommandsProvider(),
    )
    setup_dishka(container, app)
    return app