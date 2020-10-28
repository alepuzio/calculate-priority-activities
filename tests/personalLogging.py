# -*- coding: utf-8 -*-
"""Module personalLogging
Personal wrapping per logging
"""
import logging
import logging.config

class PersonalLogging:

    def __init__(self):
        logging.config.fileConfig("config-log.ini", disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
        
    def info(self, msg):
        return self.logger.info(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def debug(self, msg):
        return self.logger.debug(msg)
        
        
