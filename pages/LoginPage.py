from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):

    # Define locators as (By, Value) tuples at the class level
    EMAIL_ADDRESS_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_MESSAGE = (By.XPATH, "//div[@id='account-login']/div[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email_address(self, email_address_text: str):
        """Types the email address into the email input field."""
        self.type_into_element(email_address_text, self.EMAIL_ADDRESS_FIELD)

    def enter_password(self, password_text: str):
        """Types the password into the password input field."""
        self.type_into_element(password_text, self.PASSWORD_FIELD)

    def click_on_login_button(self) -> AccountPage:
        """Clicks the login button and returns the AccountPage instance."""
        self.element_click(self.LOGIN_BUTTON)
        return AccountPage(self.driver)

    def login_to_application(self, email_address_text: str, password_text: str) -> AccountPage:
        """Helper method to fill in credentials and submit login in one call."""
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_on_login_button()

    def retrieve_warning_message(self) -> str:
        """Retrieves and returns the warning text (e.g., for invalid credentials)."""
        return self.retrieve_element_text(self.WARNING_MESSAGE)