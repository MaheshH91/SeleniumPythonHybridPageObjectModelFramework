from datetime import datetime
import os
import re

import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utilities.ReadConfigurations import read_configuration


def pytest_addoption(parser):
    """Register custom CLI flags for pytest execution."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser options: chrome, edge, firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (default: False)",
    )


def _init_driver(request):
    """Helper function to create and configure the WebDriver instance."""
    browser_option = request.config.getoption("--browser")

    # Fallback to config.ini browser if CLI is left as default
    if not browser_option or browser_option == "chrome":
        try:
            browser = read_configuration("basic info", "browser").lower()
        except Exception:
            browser = "chrome"
    else:
        browser = browser_option.lower()

    is_headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = Options()
        if is_headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")  # Force desktop viewport in headless
            options.add_argument("--no-sandbox")             # Essential for Jenkins CI execution
            options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if is_headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Edge(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: '{browser}'. Choose from: chrome, edge, firefox")

    if not is_headless:
        driver.maximize_window()

    # Load starting application URL from config.ini
    app_url = read_configuration("basic info", "url")
    driver.get(app_url)

    # Attach driver to class instance if using Test Classes
    if request.cls is not None:
        request.cls.driver = driver

    return driver


@pytest.fixture()
def setup(request):
    """Primary setup fixture for test functions and classes."""
    driver = _init_driver(request)
    yield driver
    driver.quit()


@pytest.fixture()
def setup_and_teardown(request):
    """Alias fixture for backward compatibility with @pytest.mark.usefixtures('setup_and_teardown')."""
    driver = _init_driver(request)
    yield driver
    driver.quit()


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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and attach screenshots to BOTH
    Allure and pytest-html reports on test failures.
    """
    outcome = yield
    report = outcome.get_result()

    # Store report on item for fixture access
    setattr(item, "rep_" + report.when, report)
    extras_list = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        # Locate the driver instance attached to fixture or class
        driver = item.funcargs.get("setup") or item.funcargs.get("setup_and_teardown")
        if not driver and item.cls:
            driver = getattr(item.cls, "driver", None)

        if driver:
            screenshot_png = driver.get_screenshot_as_png()

            # 1. Attach screenshot to Allure Report
            allure.attach(
                screenshot_png,
                name="failed_test_screenshot",
                attachment_type=AttachmentType.PNG,
            )

            # 2. Attach screenshot to pytest-html Report
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            safe_nodeid = re.sub(r"[^\w\-_.]", "_", report.nodeid)
            screenshot_path = os.path.join(screenshot_dir, f"{safe_nodeid}.png")

            driver.save_screenshot(screenshot_path)

            if os.path.exists(screenshot_path):
                html_embed = (
                    f'<div><img src="{screenshot_path}" alt="screenshot" '
                    f'style="width:300px; height:auto; margin:10px 0;" '
                    f'onclick="window.open(this.src)"/></div>'
                )
                extras_list.append(extras.html(html_embed))

    report.extras = extras_list


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configures HTML report destination path and custom metadata."""
    reports_dir = os.path.join(os.curdir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    time_stamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    config.option.htmlpath = os.path.abspath(
        os.path.join(reports_dir, f"report_{time_stamp}.html")
    )

    if hasattr(config, "_metadata"):
        config._metadata.update({
            "Project Name": "Opencart / TutorialsNinja",
            "Module Name": "Customer Registration & Search",
            "Tester": "Mahesh",
        })


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """Cleans up default system metadata keys from the HTML report header."""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)