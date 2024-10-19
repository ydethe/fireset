#
# Fireset
# Copyright (C) 2016-2017 Jelmer Vernooĳ <jelmer@jelmer.uk>, et al.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 3
# of the License or (at your option) any later version of
# the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

"""CalDAV/CardDAV server."""

import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl
import logfire
import sentry_sdk
from rich.logging import RichHandler
from .LogPushoverHandler import LogPushoverHandler


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    fireset_user: str
    fireset_password: str
    logfire_token: str
    database_uri: AnyUrl
    phantombuster_key: str
    phantombuster_listid: int
    loglevel: str = "info"
    pushover_app_token: str
    pushover_user_key: str

    directory: str = "data"
    paranoid: bool = False
    index_threshold: int | None = None
    current_user_principal: str = "user"
    autocreate: bool = True
    defaults: bool = True
    strict: bool = False
    sentry_dsn: str = ""


settings = Settings()

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger("fireset_logger")
logger.setLevel(settings.loglevel.upper())

handler = RichHandler()
logger.addHandler(handler)

if settings.logfire_token != "":
    logfire.configure(token=settings.logfire_token, console=False)
    logger.addHandler(logfire.LogfireLoggingHandler())

if settings.pushover_app_token != "":
    pushover_handler = LogPushoverHandler(
        token=settings.pushover_app_token, user=settings.pushover_user_key, priority=logging.ERROR
    )
    logger.addHandler(pushover_handler)

if settings.sentry_dsn != "":
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
