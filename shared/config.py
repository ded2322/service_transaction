import environ
import logging
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(BASE_DIR / '.env')

class Settings(BaseSettings):
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{env('DB_USER')}:{env('DB_PASSWORD')}@{env('DB_HOST')}:{env('DB_PORT')}/{env('DB_NAME')}"
    
    SECRET_KEY: str = env("SECRET_KEY")
    ALGORITHM: str = env("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = env("ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings()