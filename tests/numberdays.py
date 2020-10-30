# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the date
"""

from personalLogging import PersonalLogging
from csvtime import CSVTime
from rowtime import RowTime
from state import State
from datetime import date
from datetime import datetime
import unittest


class NumberDays:
    """
    It calculate the remain number of days of an activity
    """
    def __init__(self, newState):
        self.state = newState
        #self.log = PersonalLogging()

    def days(self):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  #TODO centralize ina classe
        if "future" == self.state.state():
            res = self.number( today, self.state.start )
        elif "late" == self.state.state():
            res = self.number( self.state.end, today )
        elif "running" == self.state.state():
            res = self.number( today, self.state.end )
        else:
            raise Exception("Unkown state [{0}]".format (  self.state.state() ) )
        return res

    def number(self, one, two):
        """

        """
        return (two - one).days +1

    def __repr__(self):
        return "NumberDays[{0}]".format ( str ( self.state ) ) 

class TestNumberDays(unittest.TestCase):

    def test_days_running(self):
        one = datetime(2009, 12, 2, 10, 24, 34, 198130)
        two = datetime(2021, 10, 5, 10, 24, 34, 198130)
        state = State(one, two)
        result = NumberDays(state).days()
        expected = 341
        self.assertEqual( result , expected)

    def test_days_future(self):
        one = datetime(2023, 12, 2, 10, 24, 34, 198130)
        two = datetime(2024, 10, 5, 10, 24, 34, 198130)
        result = NumberDays( State (one, two)).days()
        expected = 1129
        self.assertEqual( result , expected)


