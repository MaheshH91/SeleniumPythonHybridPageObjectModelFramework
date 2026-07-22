from configparser import ConfigParser, NoOptionError, NoSectionError
from pathlib import Path

# Dynamically locate the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "configurations" / "config.ini"


def read_configuration(category: str, key: str) -> str:
    """
    Reads a value from the central configurations/config.ini file.

    :param category: Section name inside config.ini (e.g., 'basic info')
    :param key: Property key name (e.g., 'browser' or 'url')
    :return: The string value associated with the specified key.
    """
    config = ConfigParser()

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file not found at path: '{CONFIG_PATH}'"
        )

    config.read(CONFIG_PATH)

    try:
        return config.get(category, key)
    except NoSectionError:
        raise NoSectionError(
            f"Section '[{category}]' was not found in '{CONFIG_PATH.name}'."
        )
    except NoOptionError:
        raise NoOptionError(
            f"Key '{key}' was not found under section '[{category}]' in '{CONFIG_PATH.name}'."
        )