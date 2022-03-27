from re import S
from pydantic import BaseSettings

from app import database

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_username: str
    database_name: str
    database_password: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()