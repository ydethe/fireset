from logging.handlers import HTTPHandler
from logging import makeLogRecord
import logging


class LogPushoverHandler(HTTPHandler):
    priorities = {"DEBUG": -2, "INFO": -1, "WARNING": -1, "ERROR": 0, "CRITICAL": 1}

    def __init__(self, token: str, user: str, priority: int):
        HTTPHandler.__init__(
            self, host="api.pushover.net", url="/1/messages.json", method="POST", secure=True
        )
        self.params = {"token": token, "user": user, "priorities": self.priorities}
        self.priority = priority

    def emit(self, record: logging.LogRecord):
        if record.levelno < self.priority:
            return

        record_dict = self.mapLogRecord(record)
        record_dict["priority"] = self.params["priorities"][record_dict["levelname"]]
        record_dict["timestamp"] = record_dict["created"]
        record_dict["message"] = self.format(record)
        for key, value in self.params.items():
            record_dict[key] = value
        record = makeLogRecord(record_dict)
        HTTPHandler.emit(self, record)
