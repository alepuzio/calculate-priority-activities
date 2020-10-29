import unittest
import datetime import date

class State:

        """
        It calculate the state of an activity
        """

    def __init__(self, newStartDate, newEndDate):
        self.start = newStartDate
        self.log = PersonalLogging()
        self.end = newEndDate


    def state(self):
        res = None
        today = date.today() 
        if today < self.start:
            res = "future"
        elif self.start < today and today < self.end:
            res = "running"
        elif self.end < today
            res = "late"
        else:
            raise Exception ("Unkown state of the temporal range [{0}-{1}]".format (self.start, self.end) )
        return res 
    
    def days(self):
        res = None
        today = date.today() 
        if today < self.start:
            res = NumberDays(self.start, today)
        elif self.start < today and today < self.end:
            res = NumberDays(today, self.end)
        elif self.end < today
            res = NumberDays(self.end, today)
        else
            raise Exception ("Unkown number of days of the temporal range [{0}-{1}]".format (self.start, self.end) )
        return res.days()
