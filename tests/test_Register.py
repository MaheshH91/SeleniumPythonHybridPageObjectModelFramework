from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils
from utilities.logger import get_logger

# Initialize logger for TestRegister suite
logger = get_logger("TestRegister")


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        logger.info("--- Starting test_register_with_mandatory_fields ---")

        home_page = HomePage(self.driver)
        logger.info("Navigating to Register Page...")
        register_page = home_page.navigate_to_register_page()

        first_name = ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest", 2, 1)
        last_name = ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest", 2, 2)
        generated_email = self.generate_email_with_time_stamp()

        logger.info(
            f"Submitting registration with mandatory fields [User: {first_name} {last_name}, Email: {generated_email}]...")
        account_success_page = register_page.register_an_account(
            first_name,
            last_name,
            generated_email,
            "1234567890",
            "12345",
            "12345",
            "no",
            "select"
        )

        expected_heading = "Your Account Has Been Created!"
        actual_heading = account_success_page.retrieve_account_creation_message()

        logger.info(f"Verifying account creation message. Expected: '{expected_heading}' | Actual: '{actual_heading}'")
        assert actual_heading == expected_heading
        logger.info("PASSED: test_register_with_mandatory_fields")

    def test_register_with_all_fields(self):
        logger.info("--- Starting test_register_with_all_fields ---")

        home_page = HomePage(self.driver)
        logger.info("Navigating to Register Page...")
        register_page = home_page.navigate_to_register_page()

        generated_email = self.generate_email_with_time_stamp()
        logger.info(
            f"Submitting registration with all fields including newsletter subscription [Email: {generated_email}]...")

        account_success_page = register_page.register_an_account(
            "Mahesh",
            "Patil",
            generated_email,
            "1234567890",
            "12345",
            "12345",
            "yes",
            "select"
        )

        expected_heading = "Your Account Has Been Created!"
        actual_heading = account_success_page.retrieve_account_creation_message()

        logger.info(f"Verifying account creation message. Expected: '{expected_heading}' | Actual: '{actual_heading}'")
        assert actual_heading == expected_heading
        logger.info("PASSED: test_register_with_all_fields")

    def test_register_with_duplicate_email(self):
        logger.info("--- Starting test_register_with_duplicate_email ---")

        home_page = HomePage(self.driver)
        logger.info("Navigating to Register Page...")
        register_page = home_page.navigate_to_register_page()

        duplicate_email = "amotooricap3@gmail.com"
        logger.info(f"Attempting registration with an already existing email: {duplicate_email}")

        register_page.register_an_account(
            "Mahesh",
            "Patil",
            duplicate_email,
            "1234567890",
            "12345",
            "12345",
            "yes",
            "select"
        )

        expected_warning = "Warning: E-Mail Address is already registered!"
        actual_warning = register_page.retrieve_duplicate_email_warning()

        logger.info(f"Checking duplicate email warning. Expected: '{expected_warning}' | Actual: '{actual_warning}'")
        assert expected_warning in actual_warning
        logger.info("PASSED: test_register_with_duplicate_email")

    def test_register_without_entering_any_fields(self):
        logger.info("--- Starting test_register_without_entering_any_fields ---")

        home_page = HomePage(self.driver)
        logger.info("Navigating to Register Page...")
        register_page = home_page.navigate_to_register_page()

        logger.info("Submitting registration form with empty fields...")
        register_page.register_an_account("", "", "", "", "", "", "no", "no")

        logger.info("Verifying all mandatory validation error warning messages...")
        has_all_warnings = register_page.verify_all_warnings(
            "Warning: You must agree to the Privacy Policy!",
            "First Name must be between 1 and 32 characters!",
            "Last Name must be between 1 and 32 characters!",
            "E-Mail Address does not appear to be valid!",
            "Telephone must be between 3 and 32 characters!",
            "Password must be between 4 and 20 characters!"
        )

        assert has_all_warnings, "One or more validation warning messages did not match expected values."
        logger.info("PASSED: test_register_without_entering_any_fields")