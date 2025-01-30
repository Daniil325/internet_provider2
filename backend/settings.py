from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "123"
    POSTGRES_DB: str = "internet_provider"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    SECRET_KEY: str = "gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt"
    ALGORITHM: str = "HS256"
    
    @property
    def get_auth_data(self):
        return {"secret_key": self.SECRET_KEY, "algorithm": self.ALGORITHM}