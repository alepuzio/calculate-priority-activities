# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the data about the project and time
"""
from datetime import date
from datetime import datetime
import unittest

class CSVTime:
    """@overview: this class contains the single row of time file"""
    def __init__(self, newrow):
        self.row = newrow
        
    def activity(self):
        return self.row['activity'].strip() 
   
    def start(self):
        return self.row['start'].strip() 

    def end(self):
        return self.row['end'].strip()
    
    def __repr__(self):
        return "CSVTime[{0}]\n>>>[{1}]\n>>>>>>>>>>[{2}]]".format(self.Activity(), self.start(), self.end())

class RowTime:
    """@overview: this class contains the single row of time file"""
    def __init__(self, newActivity, newStart, newEnd):
        self.activity = newActivity
        self.start = newStart
        self.end = newEnd
    
    def __repr__(self):
        return "RowTime:{0}[{1}-{2}]".format(self.activity, self.start, self.end)

class TimeActivity:
    def __init__(self, newDayActivity):
        self.dayActivity = newDayActivity

    def days(self):
        """
        it offer the number of days in a Activity
        """        
        return ( self.dayActivity.end1() - self.dayActivity.start() ).days +1 

    def activity():
        return self.dayActivity.action()

    def __repr__(self):
        return "TimeActivity:[{0}]".format(self.ActivityTime)

class DayActivity:
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
        @return obejct date
        """
        return datetime.strptime(dateAsString, "%d/%m/%Y").date()

class GroupActivity:
    def __init__(self, newReadRows):
        self.readRows = newReadRows

    def __str__(self):
        return "GroupActivity:{0}".format(str( self.readRows ) )
    
    def __repr__(self):
        data = self.readRows
        return "GroupActivity[{0}]\n>[{1}]".format( len (data), data )
    
    def rows(self):
        """
        @return the list of Activities
        """
        return self.readRows
    

class GroupTime:    
    def rows(self, reader):
        """
        @return the list of the time datas of the Activities
        """
        result = []
        for row in reader:
            tmp = CSVTime(row)
            result.append ( DayActivity( RowTime ( tmp.activity(), tmp.start(), tmp.end() ) ) )
        return result

class TestTimeActivity(unittest.TestCase):
    def test_days(self):
        row = RowTime("Activity", "01/06/2020", "20/06/2020")
        result = TimeActivity( DayActivity ( row) ).days()
        expected = 20
        self.assertEqual(result, expected)

class TestDayActivity(unittest.TestCase):
    def test_date_ok(self):
        row = RowTime("Activity", "01/06/2020", "20/06/2020")
        var = DayActivity ( row )
        result = var.ddmmyyyy("20/06/2020")
        expected = date(2020, 6, 20)
        self.assertEqual ( result, expected )
