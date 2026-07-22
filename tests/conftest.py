import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ReadConfigurations


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Stores the execution report status on the test node so fixtures can inspect failures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request):
    """Automatically captures an Allure screenshot if the test fails."""
    yield
    item = request.node
    # Check if the call phase failed
    if hasattr(item, "rep_call") and item.rep_call.failed:
        # Retrieve the driver instance attached to the test class
        driver = getattr(request.cls, "driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failed_test_screenshot",
                attachment_type=AttachmentType.PNG
            )


@pytest.fixture()
def setup_and_teardown(request):
    """Initializes and tears down the requested WebDriver instance."""
    browser = ReadConfigurations.read_configuration("basic info", "browser").lower()
    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Invalid browser '{browser}'. Choose from: chrome, firefox, edge")

    driver.maximize_window()

    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)

    # Attach driver to the test class instance
    request.cls.driver = driver

    yield

    driver.quit()