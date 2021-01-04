import os
import importlib
import logging


def import_all_from(module: str) -> None:
    """
    Import all names from module into current globals.
    This is basically like `import *`, except it does not respect __all__,
    which is not a problem, because that is not used in django settings.
    """
    items = importlib.import_module(module).__dict__
    globals().update(items)


env = os.environ.get("SETTINGS_ENV", None)

if env is None:
    raise ValueError("SETTINGS_ENV is required")

import_all_from(f"backend.settings.envs.{env}")

log_level = logging.INFO

logging_debug = os.environ.get("SETTINGS_LOGGING_DEBUG")

if logging_debug:
    log_level = logging.DEBUG

init_logging(log_level=log_level, log_console=True)