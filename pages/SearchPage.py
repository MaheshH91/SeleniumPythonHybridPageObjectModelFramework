from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SearchPage(BasePage):

    # Define locators as (By, Value) tuples at the class level
    VALID_HP_PRODUCT_LINK = (By.LINK_TEXT, "HP LP3065")
    NO_PRODUCT_MESSAGE = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_valid_product(self) -> bool:
        """Checks and returns whether the HP LP3065 product link is visible."""
        return self.check_display_status_of_element(self.VALID_HP_PRODUCT_LINK)

    def retrieve_no_product_message(self) -> str:
        """Retrieves and returns the text displayed when no product matches search."""
        return self.retrieve_element_text(self.NO_PRODUCT_MESSAGE)