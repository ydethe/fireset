from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl


# Configuration class
class Settings(BaseSettings):
    server_url: AnyHttpUrl


settings = Settings()
