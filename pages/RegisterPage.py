from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    # Define locators as (By, Value) tuples
    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    TELEPHONE_FIELD = (By.ID, "input-telephone")
    PASSWORD_FIELD = (By.ID, "input-password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "input-confirm")
    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")
    YES_NEWSLETTER_RADIO = (By.XPATH, "//input[@name='newsletter'][@value='1']")
    MAIN_WARNING_BANNER = (By.XPATH, "//div[@id='account-register']/div[1]")

    # Field warning locators
    FIRST_NAME_WARNING = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    LAST_NAME_WARNING = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    EMAIL_WARNING = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
    TELEPHONE_WARNING = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
    PASSWORD_WARNING = (By.XPATH, "//input[@id='input-password']/following-sibling::div")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name_text: str):
        self.type_into_element(first_name_text, self.FIRST_NAME_FIELD)

    def enter_last_name(self, last_name_text: str):
        self.type_into_element(last_name_text, self.LAST_NAME_FIELD)

    def enter_email(self, email_text: str):
        self.type_into_element(email_text, self.EMAIL_FIELD)

    def enter_telephone(self, telephone_text: str):
        self.type_into_element(telephone_text, self.TELEPHONE_FIELD)

    def enter_password(self, password_text: str):
        self.type_into_element(password_text, self.PASSWORD_FIELD)

    def enter_password_confirm(self, password_text: str):
        self.type_into_element(password_text, self.CONFIRM_PASSWORD_FIELD)

    def select_agree_checkbox_field(self):
        self.element_click(self.AGREE_CHECKBOX)

    def select_yes_radio_button(self):
        self.element_click(self.YES_NEWSLETTER_RADIO)

    def click_on_continue_button(self) -> AccountSuccessPage:
        self.element_click(self.CONTINUE_BUTTON)
        return AccountSuccessPage(self.driver)

    def register_an_account(
            self,
            first_name_text: str,
            last_name_text: str,
            email_text: str,
            telephone_text: str,
            password_text: str,
            password_confirm_text: str,
            yes_or_no: str,
            privacy_policy: str
    ) -> AccountSuccessPage:
        """Fills out the registration form and submits it."""
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_confirm_text)

        if yes_or_no.lower() == "yes":
            self.select_yes_radio_button()

        if privacy_policy.lower() == "select":
            self.select_agree_checkbox_field()

        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self) -> str:
        return self.retrieve_element_text(self.MAIN_WARNING_BANNER)

    def retrieve_privacy_policy_warning(self) -> str:
        return self.retrieve_element_text(self.MAIN_WARNING_BANNER)

    def retrieve_first_name_warning(self) -> str:
        return self.retrieve_element_text(self.FIRST_NAME_WARNING)

    def retrieve_last_name_warning(self) -> str:
        return self.retrieve_element_text(self.LAST_NAME_WARNING)

    def retrieve_email_warning(self) -> str:
        return self.retrieve_element_text(self.EMAIL_WARNING)

    def retrieve_telephone_warning(self) -> str:
        return self.retrieve_element_text(self.TELEPHONE_WARNING)

    def retrieve_password_warning(self) -> str:
        return self.retrieve_element_text(self.PASSWORD_WARNING)

    def verify_all_warnings(
            self,
            expected_privacy_policy_warning: str,
            expected_first_name_warning_message: str,
            expected_last_name_warning_message: str,
            expected_email_warning_message: str,
            expected_telephone_warning_message: str,
            expected_password_warning_message: str
    ) -> bool:
        """Validates that all onscreen validation warnings match expected strings."""
        privacy_status = actual_privacy_policy_warning in expected_privacy_policy_warning if (
            actual_privacy_policy_warning := self.retrieve_privacy_policy_warning()
        ) else False

        return all([
            privacy_status,
            self.retrieve_first_name_warning() == expected_first_name_warning_message,
            self.retrieve_last_name_warning() == expected_last_name_warning_message,
            self.retrieve_email_warning() == expected_email_warning_message,
            self.retrieve_telephone_warning() == expected_telephone_warning_message,
            self.retrieve_password_warning() == expected_password_warning_message,
        ])