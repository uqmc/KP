#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Provides interface for accessing environment variables
    as configuration.
"""

import os
import logging

from utils.types import string_to_bool


class Config:
    try:
        __PROD = string_to_bool(os.getenv("PRODUCTION", "no"))
        __LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    except Exception as ex:
        logging.error(ex)
        exit(1)

    def get_is_production(self):
        return self.__PROD

    def get_log_level(self):
        return self.__LOG_LEVEL
