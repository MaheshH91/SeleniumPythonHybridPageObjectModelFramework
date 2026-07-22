from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:

    @staticmethod
    def generate_email_with_time_stamp(prefix: str = "maheshkumar", domain: str = "gmail.com") -> str:
        """Generates a unique timestamped email address for dynamic test execution."""
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"{prefix}_{timestamp}@{domain}"