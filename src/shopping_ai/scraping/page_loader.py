import time

from shopping_ai.utils.logger import (
    get_logger
)


logger = get_logger(__name__)


class PageLoader:

    @staticmethod
    def wait_for_page():

        logger.info(
            "Waiting for page load"
        )

        time.sleep(5)