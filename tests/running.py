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
    """
    def start(self):
        pass

    def end(self):
        pass
    """

class Running(TimeActivity):
    """
    base case
    """
    def __init__(self, newDayActivity):
        self.dayActivity = newDayActivity
        self.log = PersonalLogging()
        self.log.debug ( "Running", "init", "start:" + str ( self.dayActivity ) )

    def days(self):
        res = 0
        start = NumberDays( self.dayActivity.start1(), date.today() )
        self.log.warning ( "Running", "days", "start:" + str ( start ) )
        end  = NumberDays(  date.today() , self.dayActivity.end1() )
        if start.correct()  and  end.correct():
            res = end.days()
        else:
            raise Exception ("Uncorrect temporal range for project [{0}]".format ( self.dayActivity ) )
        return res
 
    def action(self):
        return self.dayActivity.action()

    def __repr__(self):
        return "Running:[{0}]".format(self.dayActivity)



class Late(TimeActivity):
    """
    case of past activtiy not yet done
    """
    def __init__(self, newTimeActivity):
        self.timeActivity = newTimeActivity
        self.log = PersonalLogging()
        self.log.debug ( "Late", "init", "start:" + str ( self.timeActivity ) )

    def days(self):
        res = 0
        days = NumberDays( self.timeActivity.end1(), date.today() )
        self.log.warning ( "Late", "days", "start:" + str ( start ) )
        if days.correct():
            res = days.days()
        else:
            raise Exception ("Uncorrect temporal range for project [{0}]".format ( self.timeActivity ) )
        return res
 
    def action(self):
        return self.timeActivity.action()

    def __repr__(self):
        return "Late:[{0}]".format(self.timeActivity)




