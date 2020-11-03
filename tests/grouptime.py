# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the date
"""

from personalLogging import PersonalLogging
from csvtime import CSVTime
from rowtime import RowTime
from running import Late
from running import Running
from dayactivity import DayActivity
from datetime import date
from datetime import datetime
from state import State
from numberdays import NumberDays
import unittest



class GroupTime:
    """
    list of DayActivity
    """
    def rows(self, reader):
        """
        @return the list of the time datas of the Activities
        """
        result = []
        for row in reader:
            tmp = CSVTime(row)
            day =  DayActivity ( RowTime ( tmp.activity(), tmp.start(), tmp.end() ) ) 
            result.append ( Late ( Running ( State ( NumberDays ( day.action() , day.start1(), day.end1()  ) ) ) ) ) 
        return result

