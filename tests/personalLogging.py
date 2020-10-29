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
        
    def info(self, nameclass, method, msg):
        if msg is None:
            return self.logger.info( "'{0}'.'{1}': none".format (nameclass, method) )
        else:
            return self.logger.info( "'{0}'.'{1}': '{2}'".format( nameclass, method, msg))

    def warning(self, nameclass, method, msg):
        if msg is None:
            return self.logger.warning( "'{0}'.'{1}': none".format (nameclass, method) )
        else:
            return self.logger.warning( "'{0}'.'{1}': '{2}'".format( nameclass, method, msg))

    def debug(self, nameclass, method, msg): 
        if msg is None:
            return self.logger.debug ( "'{0}'.'{1}': none".format (nameclass, method) )
        else:
            return self.logger.debug ( "'{0}'.'{1}': '{2}'".format( nameclass, method, msg))


        
        
