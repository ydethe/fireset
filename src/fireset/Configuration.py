from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl
import logfire


# See logfire: https://logfire.pydantic.dev/ydethe/fireset

# Configuration class
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    server_url: AnyHttpUrl
    logfire_token: str


settings = Settings()

logfire.configure(token=settings.logfire_token)
