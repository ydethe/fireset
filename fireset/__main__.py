# Xandikos
# Copyright (C) 2016-2018 Jelmer Vernooĳ <jelmer@jelmer.uk>, et al.
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

"""Xandikos command-line handling."""

import asyncio
from typing_extensions import Annotated

import typer

app = typer.Typer()


@app.command()
def main(
    directory: Annotated[str, typer.Option(help="Directory that stores the data")] = "data",
    paranoid: Annotated[bool, typer.Option(help="Paranoid mode")] = False,
    index_threshold: Annotated[int | None, typer.Option(help="Index threshold")] = None,
    current_user_principal: Annotated[
        str, typer.Option(help="Name of the principal user")
    ] = "user",
    autocreate: Annotated[bool, typer.Option(help="Create directory if it does not exist")] = True,
    defaults: Annotated[bool, typer.Option(help="Fill data with defaults")] = True,
    strict: Annotated[bool, typer.Option(help="Strict mode")] = False,
    route_prefix: Annotated[str, typer.Option(help="Route prefix")] = "/",
    listen_address: Annotated[str, typer.Option(help="Address to listen on")] = "0.0.0.0",
    port: Annotated[int, typer.Option(help="Port to listen on")] = 8000,
    metrics_port: Annotated[int, typer.Option(help="Port to listen on for metric")] = 8001,
):
    # For now, just invoke fireset.web
    from .web import main_web_run

    return asyncio.run(
        main_web_run(
            directory,
            paranoid,
            index_threshold,
            current_user_principal,
            autocreate,
            defaults,
            strict,
            route_prefix,
            listen_address,
            port,
            metrics_port,
        )
    )


if __name__ == "__main__":
    app()
