# -*- coding: utf-8 -*-
"""

.. include:: ../../README.md

# Testing

## Run the tests

To run tests, just run:

    pdm run pytest

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
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    server_url: AnyHttpUrl
    logfire_token: str
    database_uri: AnyUrl
    port: int


settings = Settings()

logfire.configure(token=settings.logfire_token)

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger("fireset_logger")
logger.setLevel(os.environ.get("LOGLEVEL", "INFO").upper())
logger.addHandler(logfire.LogfireLoggingHandler())
