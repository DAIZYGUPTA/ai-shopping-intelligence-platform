from shopping_ai.scraping.browser_manager import BrowserManager


browser = BrowserManager()

driver = browser.get_driver()

driver.get("https://www.google.com")

input("Press Enter To Close")

driver.quit()
