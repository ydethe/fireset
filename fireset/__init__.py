#
# Xandikos
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
import logfire
from rich.logging import RichHandler


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    fireset_user: str
    fireset_password: str
    logfire_token: str
    loglevel: str = "info"

    directory: str = "data"
    paranoid: bool = False
    index_threshold: int | None = None
    current_user_principal: str = "user"
    autocreate: bool = True
    defaults: bool = True
    strict: bool = False


settings = Settings()

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger("fireset_logger")
logger.setLevel(settings.loglevel.upper())

if settings.logfire_token != "":
    logfire.configure(token=settings.logfire_token)
    logger.addHandler(logfire.LogfireLoggingHandler())

handler = RichHandler()
logger.addHandler(handler)
