from time import sleep

from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import (
    WebDriverWait
)

from shopping_ai.config.urls import (
    MYNTRA_BASE_URL
)

from shopping_ai.config.selectors import (
    SEARCH_BOX,
    PRODUCT_CARD
)

from shopping_ai.discovery.product_parser import (
    ProductParser
)

from shopping_ai.scraping.browser_manager import (
    BrowserManager
)

from shopping_ai.utils.logger import (
    get_logger
)


logger = get_logger(__name__)


class ProductDiscovery:

    def __init__(self):

        self.browser_manager = BrowserManager()

        self.parser = ProductParser()

    def search_products(
        self,
        query: str,
        max_pages: int = 5
    ):

        driver = None

        all_products = []

        seen_product_ids = set()

        try:

            driver = (
                self.browser_manager
                .get_driver()
            )

            logger.info(
                f"Searching for: {query}"
            )

            driver.get(
                MYNTRA_BASE_URL
            )

            search_box = WebDriverWait(
                driver,
                20
            ).until(
                lambda d:
                d.find_element(
                    By.CSS_SELECTOR,
                    SEARCH_BOX
                )
            )

            #driver.get(
                #MYNTRA_BASE_URL  )

           # sleep(3)

            #search_box = driver.find_element(
              #  By.CSS_SELECTOR,  SEARCH_BOX )

            search_box.clear()

            search_box.send_keys(
                query
            )

            search_box.send_keys(
                Keys.ENTER
            )

            sleep(5)

            # ==================================
            # Crawl Multiple Pages
            # ==================================

            current_page = 1

            while current_page <= max_pages:

                logger.info(
                    f"Scraping Page {current_page}"
                )

                html = driver.page_source

                soup = BeautifulSoup(
                    html,
                    "lxml"
                )

                cards = soup.select(
                    PRODUCT_CARD
                )

                logger.info(
                    f"Found {len(cards)} cards"
                )

                # ==========================
                # DEBUG
                # ==========================

                if cards:

                    print(
                        f"\nPAGE {current_page} FIRST:",
                        cards[0].get("id")
                    )

                    print(
                        f"PAGE {current_page} LAST:",
                        cards[-1].get("id")
                    )

                # ==========================

                for card in cards:

                    try:

                        product = (
                            self.parser.parse(
                                card
                            )
                        )

                        if (
                            product.product_id
                            in seen_product_ids
                        ):
                            continue

                        seen_product_ids.add(
                            product.product_id
                        )

                        all_products.append(
                            product
                        )

                    except Exception:

                        logger.exception(
                            "Failed parsing product"
                        )

                logger.info(
                    f"Total products collected: "
                    f"{len(all_products)}"
                )

                # ==================================
                # Stop if reached max pages
                # ==================================

                if current_page >= max_pages:

                    break

                # ==================================
                # Next Page
                # ==================================

                try:

                    next_button = (
                        driver.find_element(
                            By.CSS_SELECTOR,
                            "li.pagination-next"
                        )
                    )

                    first_card_before = ""

                    if cards:

                        first_card_before = (
                            cards[0].get(
                                "id",
                                ""
                            )
                        )

                    next_button.click()

                    logger.info(
                        f"Moving to Page {current_page + 1}"
                    )

                    # Wait until first product changes

                    WebDriverWait(
                        driver,
                        15
                    ).until(
                        lambda d:
                        (
                            BeautifulSoup(
                                d.page_source,
                                "lxml"
                            )
                            .select(
                                PRODUCT_CARD
                            )[0]
                            .get(
                                "id",
                                ""
                            )
                            != first_card_before
                        )
                    )

                    current_page += 1

                except Exception:

                    logger.info(
                        "No next page found."
                    )

                    break

            logger.info(
                f"Finished crawling. "
                f"Total products: {len(all_products)}"
            )

            return all_products

        finally:

            if driver:

                self.browser_manager.quit_driver(
                    driver
                )