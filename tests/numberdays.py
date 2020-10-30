# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the date
"""

from personalLogging import PersonalLogging
from datetime import date
from datetime import datetime
import unittest


class NumberDays:
    """
    It calculate the remain number of days of an activity
    """
    def __init__(self, newName, newStartDate, newEndDate):
        self.name = newName
        self.start = newStartDate
        self.end = newEndDate
        self.log = PersonalLogging()

    def days(self):
        res = None
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  #TODO centralize ina classe
        if self.running(today) :#running
            res = self.number( today , self.end )
        elif self.future( today ) > 0:#future
            res = self.number( today , self.start )
        elif self.late(today): #late
            res = self.number( self.end, today )
        else:
            raise Exception ("Activity[{0}] has unkown temporal range [{1}-{2}]".format (self.name, self.start, self.end) )
        return res 


    def running (self, today):
        return self.number(today, self.start) < 0 and self.number(today, self.end) > 0 

    def future ( self, today ):
        return self.number(today, self.start) > 0
    
    def late ( self, today ) :
        return self.number( self.end , today) > 0


    def number(self, one, two):
        """
        return the number of days between two dates : if the one and two parames are equals, the result is 1
        """
        return (two - one).days

    def activity ( self ) : 
        return self.name()

    def __repr__(self):
        return "NumberDays({0},{1},{2})".format ( self.name, self.start, self.end )
        
    def __str__(self):
        return "NumberDays[{0}]-[{1}-{2}]".format ( self.name, self.start, self.end )


class TestNumberDays(unittest.TestCase):

    def test_number_same_day(self):
        one = datetime(2020, 10, 30, 10, 24, 34, 198130)
        two = datetime(2020, 10, 30, 10, 24, 34, 198130)
        result = NumberDays("number", one, two).number(one, two)
        expected = 0
        self.assertEqual( result , expected)
    
    def test_number_different_days(self):    
        one = datetime(2020, 10, 29, 10, 24, 34, 198130)
        two = datetime(2020, 10, 30, 10, 24, 34, 198130)
        result = NumberDays("number", one, two).number(one, two)
        expected = 1
        self.assertEqual( result , expected)
    
    def test_days_running(self):
        one = datetime(2020, 10, 29, 10, 24, 34, 198130)
        two = datetime(2020, 10, 31, 10, 24, 34, 198130)
        result = NumberDays("activity-running", one, two).days()
        expected = 1
        self.assertEqual( result , expected)

    def test_days_future(self):
        one = datetime(2023, 12, 2, 10, 24, 34, 198130)
        two = datetime(2024, 10, 5, 10, 24, 34, 198130)
        result = NumberDays( "activity-future", one, two ).days()
        expected = 1128
        self.assertEqual( result , expected)


