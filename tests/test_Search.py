from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities.logger import get_logger

# Initialize logger for TestSearch suite
logger = get_logger("TestSearch")


class TestSearch(BaseTest):

    def test_search_for_a_valid_product(self):
        logger.info("--- Starting test_search_for_a_valid_product ---")

        product_name = "HP"
        home_page = HomePage(self.driver)
        logger.info(f"Searching for valid product: '{product_name}'...")
        search_page = home_page.search_for_a_product(product_name)

        logger.info("Verifying valid search product display status...")
        is_product_displayed = search_page.display_status_of_valid_product()

        assert is_product_displayed, (
            "Valid search product (HP LP3065) was not displayed."
        )
        logger.info("PASSED: test_search_for_a_valid_product")

    def test_search_for_an_invalid_product(self):
        logger.info("--- Starting test_search_for_an_invalid_product ---")

        product_name = "Honda"
        home_page = HomePage(self.driver)
        logger.info(f"Searching for invalid product: '{product_name}'...")
        search_page = home_page.search_for_a_product(product_name)

        expected_text = "There is no product that matches the search criteria."
        actual_text = search_page.retrieve_no_product_message()

        logger.info(f"Checking no-product message. Expected: '{expected_text}' | Actual: '{actual_text}'")
        assert actual_text == expected_text
        logger.info("PASSED: test_search_for_an_invalid_product")

    def test_search_without_entering_any_product(self):
        logger.info("--- Starting test_search_without_entering_any_product ---")

        home_page = HomePage(self.driver)
        logger.info("Performing empty search without entering any product name...")
        search_page = home_page.search_for_a_product("")

        expected_text = "There is no product that matches the search criteria."
        actual_text = search_page.retrieve_no_product_message()

        logger.info(f"Checking no-product message. Expected: '{expected_text}' | Actual: '{actual_text}'")
        assert actual_text == expected_text
        logger.info("PASSED: test_search_without_entering_any_product")