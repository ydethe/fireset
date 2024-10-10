import asyncio

from aiohttp import BasicAuth, web
from aiohttp.test_utils import AioHTTPTestCase, TestClient, TestServer

from fireset import settings
from fireset.web import main_web_build_app


class MyAppTestCase(AioHTTPTestCase):
    async def get_application(self):
        """
        Override the get_application method to return your application.
        """
        app = await main_web_build_app()
        return app

    async def get_client(self, server: TestServer) -> TestClient:
        """Return a TestClient instance."""
        auth = BasicAuth(settings.fireset_user, settings.fireset_password)
        return TestClient(server, loop=self.loop, auth=auth)

    async def test_example(self):
        async with self.client.request("GET", "/user/contacts/addressbook") as resp:
            self.assertEqual(resp.status, 200)


def test_main():
    from fireset.web import main_web_build_app

    app = main_web_build_app()
    web.run_app(app=app, port=3665)


async def main():
    m = MyAppTestCase()
    await m.asyncSetUp()
    await m.test_example()
    await m.asyncTearDown()


if __name__ == "__main__":
    # test_main()

    asyncio.run(main())
