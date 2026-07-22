from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AccountPage(BasePage):

    # Define locators as (By, Value) tuples at the class level
    EDIT_ACCOUNT_INFO_LINK = (By.LINK_TEXT, "Edit your account information")

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_edit_your_account_information_option(self) -> bool:
        """Returns True if the 'Edit your account information' link is displayed."""
        return self.check_display_status_of_element(self.EDIT_ACCOUNT_INFO_LINK)

    def click_edit_account_information_option(self):
        """Clicks on the 'Edit your account information' link."""
        self.element_click(self.EDIT_ACCOUNT_INFO_LINK)