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


class NumberDays:
    """
    It calculate the remain number of days of an activity
    """
    def __init__(self, newStartDate, newEndDate):
        self.start = newStartDate
        self.log = PersonalLogging()
        self.log.warning ( "NumberDays","init", "start {0}".format ( str ( newStartDate ) ) )
        self.end = newEndDate

    def days(self):
        return (self.end - self.start ).days +1

    def correct(self):
        """
        @return true if the end field is before the start field
        """
        self.log.debug ( "NumberDays","days", "end {0}".format (str ( self.end ) ) )
        self.log.warning ( "NumberDays","days", "start {0}".format (str ( self.start ) ) )
        return ( self.end > self.start )

    def __repr__(self):
        return "NumberDays[{0}-{1}]".format ( str ( self.start ) , str ( self.end ) )

class TestNumberDays(unittest.TestCase):

    def test_days(self):
        one = datetime(2009, 12, 2, 10, 24, 34, 198130)
        two = datetime(2019, 10, 5, 10, 24, 34, 198130)
        result = NumberDays(one ,two).days()
        expected = 3595
        self.assertEqual( result , expected)

    def test_correct(self):
        one = datetime(2009, 12, 2, 10, 24, 34, 198130)
        two = datetime(2019, 10, 5, 10, 24, 34, 198130)
        result = NumberDays(one, two).correct()
        self.assertTrue( result )


