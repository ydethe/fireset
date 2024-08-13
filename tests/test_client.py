from starlette.testclient import TestClient

from fireset.server import app


def test_app():
    client = TestClient(
        app,
        headers={"Authorization": "Basic eWRldGhlQGdtYWlsLmNvbTphbGljZXB3ZA=="},
        follow_redirects=False,
    )
    response = client.get("/.well-known/carddav")
    assert response.status_code == 302
    response = client.options("/users/52")
    assert response.status_code == 200
    response = client.request(method="PROPFIND", url="/users/52")
    assert response.status_code == 200
    response = client.options("/users/52/addressbooks")
    assert response.status_code == 200
    response = client.request(method="PROPFIND", url="/users/52/addressbooks")
    assert response.status_code == 200
    response = client.get("/users/52/addressbooks/main/52.vcf")
    assert response.status_code == 200


if __name__ == "__main__":
    test_app()
