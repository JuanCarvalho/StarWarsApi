import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    app_name: str = "StarWars API"
    api_version: str = "v1"

    mongodb_host: str = "localhost"
    mongodb_port: int = 27017


settings = Settings()
