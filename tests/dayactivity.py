# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the date
"""

from personalLogging import PersonalLogging
from csvtime import CSVTime
from rowtime import RowTime
from datetime import date
from datetime import datetime
import unittest


class DayActivity:
    """
    Abstract represensation of the data by CSV row of project-date
    """
    def __init__(self, newRowTime):
        self.rowTime = newRowTime
        self.log = PersonalLogging()

    def start1(self):    
        self.log.warning ( "DayActivity" , "start", "{0}".format ( str ( self.rowTime.start ) ) )  
        return self.ddmmyyyy(self.rowTime.start)

    def end1(self):
        return self.ddmmyyyy(self.rowTime.end)

    def action(self):
        return self.rowTime.activity

    def ddmmyyyy(self, dateAsString):
        """
        @return object date
        """
        #return datetime.strptime(dateAsString, "%d/%m/%Y").date().replace(hour=0, minute=0, second=0, microsecond=0 )
        return datetime.strptime(dateAsString, "%d/%m/%Y").replace(hour=0, minute=0, second=0, microsecond=0 )

    def __repr__(self):
        return "DayActivity:{0}-{1}:{2}".format (self.rowTime, self.start1(), self.end1() )
    

