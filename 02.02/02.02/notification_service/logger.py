import logging
from logging.handlers import RotatingFileHandler

from config import LOG_BACKUP_COUNT, LOG_FILE, LOG_MAX_BYTES


def get_logger() -> logging.Logger:
    logger = logging.getLogger("notification_service")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        LOG_FILE, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(console)
    return logger


logger = get_logger()