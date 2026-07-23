import pytest

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils
from utilities.logger import get_logger

# Initialize logger for TestLogin suite
logger = get_logger("TestLogin")


class TestLogin(BaseTest):

    @pytest.mark.parametrize(
        "email_address,password",
        ExcelUtils.get_data_from_excel("ExcelFiles/TutorialsNinja.xlsx", "LoginTest")
    )
    def test_login_with_valid_credentials(self, email_address: str, password: str):
        logger.info(f"--- Starting test_login_with_valid_credentials [User: {email_address}] ---")

        home_page = HomePage(self.driver)
        logger.info("Navigating to Login Page...")
        login_page = home_page.navigate_to_login_page()

        logger.info("Submitting valid login credentials...")
        account_page = login_page.login_to_application(email_address, password)

        logger.info("Verifying successful login by checking Account Information option display status...")
        is_edit_displayed = account_page.display_status_of_edit_your_account_information_option()

        assert is_edit_displayed, (
            "Edit account information option was not displayed after login."
        )
        logger.info("PASSED: test_login_with_valid_credentials")

    def test_login_with_invalid_email_and_valid_password(self):
        logger.info("--- Starting test_login_with_invalid_email_and_valid_password ---")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()

        invalid_email = self.generate_email_with_time_stamp()
        logger.info(f"Attempting login with generated invalid email: {invalid_email}")
        login_page.login_to_application(invalid_email, "12345")

        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        actual_warning = login_page.retrieve_warning_message()

        logger.info(f"Checking warning message. Expected: '{expected_warning}' | Actual: '{actual_warning}'")
        assert expected_warning in actual_warning
        logger.info("PASSED: test_login_with_invalid_email_and_valid_password")

    def test_login_with_valid_email_and_invalid_password(self):
        logger.info("--- Starting test_login_with_valid_email_and_invalid_password ---")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()

        logger.info("Attempting login with valid email and invalid password...")
        login_page.login_to_application("amotooricap1@gmail.com", "1234567890")

        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        actual_warning = login_page.retrieve_warning_message()

        logger.info(f"Checking warning message. Expected: '{expected_warning}' | Actual: '{actual_warning}'")
        assert expected_warning in actual_warning
        logger.info("PASSED: test_login_with_valid_email_and_invalid_password")

    def test_login_without_entering_credentials(self):
        logger.info("--- Starting test_login_without_entering_credentials ---")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()

        logger.info("Submitting empty credentials...")
        login_page.login_to_application("", "")

        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        actual_warning = login_page.retrieve_warning_message()

        logger.info(f"Checking warning message. Expected: '{expected_warning}' | Actual: '{actual_warning}'")
        assert expected_warning in actual_warning
        logger.info("PASSED: test_login_without_entering_credentials")