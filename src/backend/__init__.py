from __future__ import absolute_import
from typing import Optional
from pathlib import Path

import logging
import os
import sys

import django.conf

default_app_config = 'backend.apps.BackendConfig'


def init_logging(
    log_level: int = logging.INFO,
    log_console: bool = False,
) -> None:
    env_log_level = os.environ.get("LOG_LEVEL", None)
    if env_log_level is not None:
        log_level = getattr(logging, env_log_level)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    console_formatter = logging.Formatter(
        style="{",
        fmt="{asctime} [{name}] [{levelname}] {message}"
    )
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.DEBUG)

    root_logger.addHandler(console_handler)
