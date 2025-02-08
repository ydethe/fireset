# -*- coding: utf-8 -*-
"""

.. include:: ../../README.md

# Testing

## Run the tests

To run tests, just run:

    pytest

## Test reports

[See test report](../tests/report.html)

[See coverage](../coverage/index.html)

.. include:: ../../CHANGELOG.md

"""
import os
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, AnyUrl
import logfire


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    server_url: AnyHttpUrl
    logfire_token: str
    repo_url: AnyUrl
    repo_token: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str

    @property
    def sqlalchemy_database_uri(self) -> str:
        db_uri = f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}/{self.postgres_db}"
        return db_uri


settings = Settings()

logfire.configure(token=settings.logfire_token)

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger("fireset_logger")
logger.setLevel(os.environ.get("LOGLEVEL", "INFO").upper())
logger.addHandler(logfire.LogfireLoggingHandler())
