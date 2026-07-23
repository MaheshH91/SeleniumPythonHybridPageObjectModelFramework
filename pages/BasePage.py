from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from utilities.logger import get_logger

# Initialize logger specifically for BasePage actions
logger = get_logger("BasePage")


class BasePage:

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self, locator: tuple):
        """Finds and returns an element after waiting for its presence in the DOM."""
        logger.info(f"Waiting for presence of element with locator: {locator}")
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logger.info(f"Successfully found element: {locator}")
            return element
        except TimeoutException:
            logger.error(f"TimeoutException: Element with locator {locator} was not found within timeout.")
            raise NoSuchElementException(
                f"Element with locator {locator} was not found within timeout."
            )

    def type_into_element(self, text: str, locator: tuple):
        """Waits for element to be clickable, clears existing text, and types input."""
        logger.info(f"Typing '{text}' into element with locator: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            element.clear()
            element.send_keys(text)
            logger.info(f"Successfully typed '{text}' into locator: {locator}")
        except Exception as e:
            logger.error(f"Failed to type '{text}' into locator {locator}. Exception: {str(e)}")
            raise e

    def element_click(self, locator: tuple):
        """Waits for element to be clickable before performing a click."""
        logger.info(f"Attempting to click on element with locator: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Successfully clicked on element with locator: {locator}")
        except Exception as e:
            logger.error(f"Failed to click on element with locator {locator}. Exception: {str(e)}")
            raise e

    def check_display_status_of_element(self, locator: tuple) -> bool:
        """Returns True if element is visible on page, False if absent or hidden."""
        logger.info(f"Checking display status of element with locator: {locator}")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            is_displayed = element.is_displayed()
            logger.info(f"Display status for {locator} is: {is_displayed}")
            return is_displayed
        except TimeoutException:
            logger.warning(f"Element with locator {locator} is not displayed/visible on page.")
            return False

    def retrieve_element_text(self, locator: tuple) -> str:
        """Retrieves inner text of an element once visible."""
        logger.info(f"Retrieving text from element with locator: {locator}")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            logger.info(f"Retrieved text '{text}' from element with locator: {locator}")
            return text
        except Exception as e:
            logger.error(f"Failed to retrieve text from locator {locator}. Exception: {str(e)}")
            raise e