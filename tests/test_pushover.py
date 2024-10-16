from fireset.pushover import send_message


def test_pushover():
    send_message("Hello poney")


if __name__ == "__main__":
    test_pushover()
