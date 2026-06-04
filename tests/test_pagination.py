from time import sleep

from selenium.webdriver.common.by import By

from shopping_ai.scraping.browser_manager import (
    BrowserManager
)

from shopping_ai.config.urls import (
    MYNTRA_BASE_URL
)


driver = (
    BrowserManager()
    .get_driver()
)

driver.get(
    f"{MYNTRA_BASE_URL}/cotton-sarees?rawQuery=cotton sarees"
)

sleep(5)

next_button = driver.find_element(
    By.CSS_SELECTOR,
    "li.pagination-next"
)

print(
    "Found Next Button"
)

next_button.click()

sleep(5)

print(
    "Clicked Next"
)

input(
    "Check browser manually. Press Enter..."
)

driver.quit()