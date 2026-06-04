import logging
from pathlib import Path

from shopping_ai.config.paths import LOG_DIR


LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

LOG_FILE = LOG_DIR / "shopping_ai.log"


def get_logger(
    logger_name: str
):

    logger = logging.getLogger(
        logger_name
    )

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        )

        file_handler.setFormatter(
            formatter
        )

        stream_handler = logging.StreamHandler()

        stream_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

        logger.addHandler(
            stream_handler
        )

    return logger