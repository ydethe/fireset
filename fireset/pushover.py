import http.client
import urllib

from . import settings


def send_message(msg: str) -> int:
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": settings.pushover_app_token,
                "user": settings.pushover_user_key,
                "message": msg,
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    r = conn.getresponse()
    return r.status
