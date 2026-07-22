from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    # Define locator as a (By, Value) tuple
    ACCOUNT_CREATION_MESSAGE = (By.XPATH, "//div[@id='content']/h1")

    def __init__(self, driver):
        super().__init__(driver)

    def retrieve_account_creation_message(self) -> str:
        """Retrieves and returns the header text confirming account creation."""
        return self.retrieve_element_text(self.ACCOUNT_CREATION_MESSAGE)