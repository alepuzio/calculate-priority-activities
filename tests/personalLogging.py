# -*- coding: utf-8 -*-
"""Module personalLogging
Personal wrapping per logging
"""
import logging
import logging.config
import os
class PersonalLogging:

    def __init__(self):
        """
        It's not polite, but in the constructor I read the file
        TODO i read the file out the constructor and I will pass the result
        from https://stackoverflow.com/questions/53222413/python-configparser-raise-keyerror-key?rq=1
        """
        path = "/".join( ( os.path.abspath( __file__ ).replace( "\\", "/" ) ).split( "/" )[:-1])
        logging.config.fileConfig( os.path.join ( path, "config-log.ini" ), disable_existing_loggers=False ) # working in local
        #logging.config.fileConfig ( "config-log.ini", disable_existing_loggers=False) # working in local
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


        
        
