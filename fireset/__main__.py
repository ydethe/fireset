# Fireset
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

"""Fireset command-line handling."""

from . import logger


def main():
    logger.info("Running server...")

    from .web import main_web_run

    return main_web_run()


if __name__ == "__main__":
    main()

    # from aiohttp import web

    # routes = web.RouteTableDef()

    # @routes.get("/")
    # async def hello(request):
    #     return web.Response(text="Hello, world")

    # app = web.Application()
    # app.add_routes(routes)
    # web.run_app(
    #     app,
    #     port=3665,
    #     access_log=logger,
    #     access_log_format='%{X-Real-Ip}i %t "%r" %s %b "%{Referer}i" "%{User-Agent}i"',
    # )
