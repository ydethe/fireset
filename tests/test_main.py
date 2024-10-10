from aiohttp import BasicAuth
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

    async def test_get_root(self):
        async with self.client.request("GET", "/") as resp:
            self.assertEqual(resp.status, 200)

    async def test_get_vcard(self):
        async with self.client.get(
            "user/contacts/addressbook/0C717D78-DBD7-44AA-8A5F-D300EF686AC6.vcf"
        ) as resp:
            self.assertEqual(resp.status, 200)
            txt = await resp.text()
        self.assertIn("BEGIN:VCARD", txt)


async def main():
    m = MyAppTestCase()

    await m.asyncSetUp()
    # await m.test_get_root()
    await m.test_get_vcard()
    await m.asyncTearDown()


if __name__ == "__main__":
    from fireset.__main__ import runserver

    runserver()

    # asyncio.run(main())
