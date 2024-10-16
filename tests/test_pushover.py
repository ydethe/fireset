from datetime import datetime

from fireset import logger


def test_pushover():
    dt = datetime.now()
    logger.debug(f"Hello debug {dt:%H:%M}")
    logger.info(f"Hello info {dt:%H:%M}")
    logger.warning(f"Hello warning {dt:%H:%M}")
    logger.error(f"Hello error {dt:%H:%M}")


if __name__ == "__main__":
    test_pushover()
