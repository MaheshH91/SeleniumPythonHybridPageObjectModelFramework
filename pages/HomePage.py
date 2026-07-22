from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):

    # Define locators as (By, Value) tuples at the class level
    SEARCH_BOX_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'btn-default')]")
    MY_ACCOUNT_DROP_MENU = (By.XPATH, "//span[text()='My Account']")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    REGISTER_OPTION = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_product_into_search_box_field(self, product_name: str):
        """Types product name into the search box."""
        self.type_into_element(product_name, self.SEARCH_BOX_FIELD)

    def click_on_search_button(self) -> SearchPage:
        """Clicks the search button and returns the SearchPage."""
        self.element_click(self.SEARCH_BUTTON)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        """Opens the 'My Account' dropdown menu."""
        self.element_click(self.MY_ACCOUNT_DROP_MENU)

    def select_login_option(self) -> LoginPage:
        """Clicks the 'Login' option in the dropdown and returns the LoginPage."""
        self.element_click(self.LOGIN_OPTION)
        return LoginPage(self.driver)

    def navigate_to_login_page(self) -> LoginPage:
        """Helper method to open dropdown and go directly to Login page."""
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def select_register_option(self) -> RegisterPage:
        """Clicks the 'Register' option in the dropdown and returns the RegisterPage."""
        self.element_click(self.REGISTER_OPTION)
        return RegisterPage(self.driver)

    def navigate_to_register_page(self) -> RegisterPage:
        """Helper method to open dropdown and go directly to Register page."""
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    def search_for_a_product(self, product_name: str) -> SearchPage:
        """Helper method to enter product and submit search in one call."""
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()