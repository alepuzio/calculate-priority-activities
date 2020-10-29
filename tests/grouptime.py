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
            #result.append ( ToStart ( Late ( Running ( DayActivity( RowTime ( tmp.activity(), tmp.start(), tmp.end() ) ) ) )) )
            result.append ( Late ( Running ( DayActivity ( RowTime ( tmp.activity(), tmp.start(), tmp.end() ) ) ) ) )
        return result

