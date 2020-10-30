# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the date
"""

from personalLogging import PersonalLogging
from csvtime import CSVTime
from rowtime import RowTime
from datetime import date
from datetime import datetime
from numberdays import NumberDays
import unittest


class TimeActivity:

    def days(self):
        """
        it offer the number of days in a Activity
        """        
        pass

    def action(self):
        pass

class Running(TimeActivity):
    """
    base case
    """
    def __init__(self, newNumberDays):
        self.numberDays = newNumberDays
        self.log = PersonalLogging()
        self.log.debug ( "Running", "init", "start:" + str ( self.numberDays ) )

    def days(self):
        return self.numberDays.days()
 
    def action(self):
        return self.numberDays.activity1()

    def __repr__(self):
        return "Running:[{0}]".format( self.numberDays )
    

class Late(TimeActivity):
    """
    case of past activtiy not yet done
    """
    def __init__(self, newTimeActivity ):
        self.timeActivity = newTimeActivity
        self.log = PersonalLogging()
        self.log.debug ( "Late", "init", "start:" + str ( self.timeActivity ) )

    def days(self):
        return self.timeActivity.days()
 
    def action(self):
        return self.timeActivity.action()
    
    def __repr__(self):
        return "Late:[{0}]".format( self.timeActivity )




