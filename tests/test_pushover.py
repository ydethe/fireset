from datetime import datetime

from fireset import logger


def test_pushover():
    dt = datetime.now()
    logger.info(f"Hello poney {dt:%H:%M}")


if __name__ == "__main__":
    test_pushover()
