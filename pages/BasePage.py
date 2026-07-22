from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self, locator: tuple):
        """Finds and returns an element after waiting for its presence in the DOM."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f"Element with locator {locator} was not found within timeout."
            )

    def type_into_element(self, text: str, locator: tuple):
        """Waits for element to be clickable, clears existing text, and types input."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator: tuple):
        """Waits for element to be clickable before performing a click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def check_display_status_of_element(self, locator: tuple) -> bool:
        """Returns True if element is visible on page, False if absent or hidden."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    def retrieve_element_text(self, locator: tuple) -> str:
        """Retrieves inner text of an element once visible."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text