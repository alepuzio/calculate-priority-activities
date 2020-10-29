# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the date
"""

from timeActivity import CSVTime
from timeActivity import RowTime
from datetime import date
from datetime import datetime
import unittest


class NumberDays:
    """
    It calculate the remain number of days of an activity
    """
    def __init__(self, newStart, newEnd):
        self.start = newStart
        self.end = newEnd

    def days(self):
        return (self.end - self.start).days +1

    def correct(self):
        """
        @return true if the end field is before the start field
        """
        return (self.end > self.start)

class TimeActivity:

    def days(self):
        """
        it offer the number of days in a Activity
        """        
        pass

    def action(self):
        pass

    def start(self):
        pass

    def end(self):
        pass
class Running(TimeActivity):
    """
    base case
    """
    def __init__(self, newDayActivity):
        self.dayActivity = newDayActivity
        
    def days(self):
        res = 0
        start = NumberDays(self.dayActivity.start(), datetime.date.today() )
        end  = NumberDays(  datetime.date.today() , self.dayActivity.end() )
        if start.correct()  & end.correct():
            res = end.days()
        else:
            raise Exception ("Uncorrect temporal range for project [{0}]".self.dayActivity)
        return res
 
    def action(self):
        return self.dayActivity.action()


    def __repr__(self):
        return "Running:[{0}]".format(self.dayActivity)

class Late(TimeActivity):
    """
    Activity with past end
    """
    def __init__(self, newTimeActivity):
        self.timeActivity = newTimeActivity
        
    def days(self):
        res = 0
        numberDays = NumberDays(  datetime.date.today(), self.timeActivity.end1() )
        if numberDays.correct() :
            res = numberDays.days()
        else:
            res = self.timeActivity.days()
        return res

    def action(self):
        return self.timeActivity.action()


    def __repr__(self):
        return "Late:[{0}]".format(self.timeActivity)

class ToStart(TimeActivity):
    """
    Activity with future begin
    """
    def __init__(self, newTimeActivity):
        self.timeActivity = newTimeActivity
        
    def days(self):
        res = 0
        numberDays = NumberDays( self.timeActivity.start(), datetime.date.today() )
        if numberDays.correct() :
            res = numberDays.days()
        else:
            res = self.timeActivity.days()
        return res

    def action(self):
        return self.timeActivity.action()


    def __repr__(self):
        return "ToStart:[{0}]".format(self.timeActivity)




class DayActivity:
    """
    Abstract represensation of the data by CSV row of project-date
    """
    def __init__(self, newRowTime):
        self.rowTime = newRowTime
        
    def start(self):        
        return self.ddmmyyyy(self.rowTime.start)

    def end1(self):
        return self.ddmmyyyy(self.rowTime.end)

    def action(self):
        return self.rowTime.activity

    def ddmmyyyy(self, dateAsString):
        """
        @return object date
        """
        return datetime.strptime(dateAsString, "%d/%m/%Y").date()

    

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
            result.append ( ToStart ( Late ( Running ( DayActivity( RowTime ( tmp.activity(), tmp.start(), tmp.end() ) ) ) )) )
        return result


class TestDayActivity(unittest.TestCase):
    def test_date_ok(self):
        row = RowTime("Activity", "01/06/2020", "20/06/2020")
        var = DayActivity ( row )
        result = var.ddmmyyyy("20/06/2020")
        expected = date(2020, 6, 20)
        self.assertEqual ( result, expected )
