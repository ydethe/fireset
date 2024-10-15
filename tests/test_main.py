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

    async def test_get_user(self):
        async with self.client.get("user/") as resp:
            self.assertEqual(resp.status, 200)

    async def test_get_contacts(self):
        async with self.client.get("user/contacts/") as resp:
            self.assertEqual(resp.status, 200)

    async def test_get_addressbook(self):
        async with self.client.get("user/contacts/addressbook/") as resp:
            self.assertEqual(resp.status, 200)

    async def test_get_vcard(self):
        async with self.client.get(
            "user/contacts/addressbook/fc652773-d10a-4d75-b040-12a6903fc9f2"
        ) as resp:
            self.assertEqual(resp.status, 200)
            txt = await resp.text()
        self.assertIn("BEGIN:VCARD", txt)


async def main():
    m = MyAppTestCase()

    await m.asyncSetUp()
    # await m.test_get_root()
    # await m.test_get_user()
    # await m.test_get_contacts()
    # await m.test_get_addressbook()
    await m.test_get_vcard()
    await m.asyncTearDown()


if __name__ == "__main__":
    from fireset.__main__ import runserver

    runserver()

    # asyncio.run(main())
