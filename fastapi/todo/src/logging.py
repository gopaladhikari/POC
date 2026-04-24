import logging
from enum import StrEnum

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class LogLevels(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


def get_logger(log_lelvel: str = LogLevels.ERROR):
    if log_lelvel not in LogLevels:
        logging.basicConfig(level=logging.ERROR)
        return

    if log_lelvel == LogLevels.DEBUG:
        logging.basicConfig(level=logging.DEBUG, format=log_format)
        return

    logging.basicConfig(level=log_lelvel)
