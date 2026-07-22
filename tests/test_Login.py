import pytest

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):

    @pytest.mark.parametrize(
        "email_address,password",
        ExcelUtils.get_data_from_excel("ExcelFiles/TutorialsNinja.xlsx", "LoginTest")
    )
    def test_login_with_valid_credentials(self, email_address: str, password: str):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application(email_address, password)


        assert account_page.display_status_of_edit_your_account_information_option(), (
            "Edit account information option was not displayed after login."
        )

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(), "12345")

        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert expected_warning in login_page.retrieve_warning_message()

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("amotooricap1@gmail.com", "1234567890")

        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert expected_warning in login_page.retrieve_warning_message()

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")

        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert expected_warning in login_page.retrieve_warning_message()