from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from shopping_ai.config.settings import (
    HEADLESS,
    IMPLICIT_WAIT,
    PAGE_LOAD_TIMEOUT
)

from shopping_ai.utils.logger import (
    get_logger
)

from shopping_ai.utils.exceptions import (
    BrowserInitializationError
)


logger = get_logger(__name__)


class BrowserManager:

    def __init__(
        self,
        headless: bool = HEADLESS
    ):
        self.headless = headless

    def get_driver(self):

        try:

            logger.info(
                "Initializing Chrome Browser"
            )

            options = webdriver.ChromeOptions()

            if self.headless:

                logger.info(
                    "Running in headless mode"
                )

                options.add_argument(
                    "--headless=new"
                )

            options.add_argument(
                "--start-maximized"
            )

            options.add_argument(
                "--disable-blink-features=AutomationControlled"
            )

            options.add_experimental_option(
                "excludeSwitches",
                ["enable-automation"]
            )

            options.add_experimental_option(
                "useAutomationExtension",
                False
            )

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            driver.implicitly_wait(
                IMPLICIT_WAIT
            )

            driver.set_page_load_timeout(
                PAGE_LOAD_TIMEOUT
            )

            logger.info(
                "Chrome Browser Started Successfully"
            )

            return driver

        except Exception as e:

            logger.exception(
                "Failed to initialize browser"
            )

            raise BrowserInitializationError(
                str(e)
            ) from e

    def quit_driver(
        self,
        driver
    ):

        try:

            if driver:

                logger.info(
                    "Closing Browser"
                )

                driver.quit()

        except Exception:

            logger.exception(
                "Failed while closing browser"
            )