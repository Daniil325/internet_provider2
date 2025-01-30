from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from backend.settings import Settings


def pg_url(
    pg_user: str, pg_password: str, pg_host: str, pg_port: str, pg_db: str
) -> str:
    return f"{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"


def build_url(pg_user: str, pg_password: str, pg_host: str, pg_port: str, pg_db: str):
    return f"postgresql+asyncpg://{pg_url(pg_user, pg_password, pg_host, pg_port, pg_db)}"


class PostgresSession:

    def __init__(self):
        config = Settings()
        self.async_session: AsyncSession = async_sessionmaker(
            bind=create_async_engine(
                url=build_url(
                    config.POSTGRES_USER,
                    config.POSTGRES_PASSWORD,
                    config.POSTGRES_HOST,
                    config.POSTGRES_PORT,
                    config.POSTGRES_DB,
                ),
                echo=True,
            )
        )
        
    def get_async(self) -> AsyncSession:
        return self.async_session
