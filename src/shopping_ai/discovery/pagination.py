from time import sleep

from selenium.webdriver.common.by import By

from shopping_ai.config.selectors import (
    PAGINATION_NEXT,
    PAGINATION_DISABLED
)

from shopping_ai.utils.logger import (
    get_logger
)


logger = get_logger(__name__)


class PaginationManager:

    def has_next_page(
        self,
        driver
    ) -> bool:

        try:

            next_button = driver.find_element(
                By.CSS_SELECTOR,
                PAGINATION_NEXT
            )

            classes = next_button.get_attribute(
                "class"
            )

            return (
                PAGINATION_DISABLED
                not in classes
            )

        except Exception:

            logger.exception(
                "Failed checking next page"
            )

            return False

    def go_to_next_page(
        self,
        driver
    ) -> bool:

        try:

            next_button = driver.find_element(
                By.CSS_SELECTOR,
                PAGINATION_NEXT
            )

            driver.execute_script(
                "arguments[0].click();",
                next_button
            )

            sleep(3)

            logger.info(
                "Moved to next page"
            )

            return True

        except Exception:

            logger.exception(
                "Failed moving to next page"
            )

            return False