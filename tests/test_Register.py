from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        account_success_page = register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest", 2, 1),
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest", 2, 2),
            self.generate_email_with_time_stamp(),
            "1234567890",
            "12345",
            "12345",
            "no",
            "select"
        )

        expected_heading = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message() == expected_heading

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        account_success_page = register_page.register_an_account(
            "Arun",
            "Motoori",
            self.generate_email_with_time_stamp(),
            "1234567890",
            "12345",
            "12345",
            "yes",
            "select"
        )

        expected_heading = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message() == expected_heading

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        register_page.register_an_account(
            "Arun",
            "Motoori",
            "amotooricap3@gmail.com",
            "1234567890",
            "12345",
            "12345",
            "yes",
            "select"
        )

        expected_warning = "Warning: E-Mail Address is already registered!"
        assert expected_warning in register_page.retrieve_duplicate_email_warning()

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        register_page.register_an_account("", "", "", "", "", "", "no", "no")

        assert register_page.verify_all_warnings(
            "Warning: You must agree to the Privacy Policy!",
            "First Name must be between 1 and 32 characters!",
            "Last Name must be between 1 and 32 characters!",
            "E-Mail Address does not appear to be valid!",
            "Telephone must be between 3 and 32 characters!",
            "Password must be between 4 and 20 characters!"
        ), "One or more validation warning messages did not match expected values."