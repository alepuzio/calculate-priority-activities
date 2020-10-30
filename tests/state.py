import unittest
from datetime import date
from datetime import datetime
from personalLogging import PersonalLogging

class State:

        """
        It calculate the state of an activity
        """
        def __init__(self, newName, newStartDate, newEndDate):
            self.name = newName
            self.start = newStartDate
            self.end = newEndDate
            self.log = PersonalLogging()

        def activity(self):
            return self.name

        def state(self):
            res = None
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  #TODO centralize ina classe
            if (today - self.start).days < 0:
                res = "future"
            elif (self.start - today).days <0 and (today - self.end).days < 0 :
                res = "running"
            elif (self.end - today).days < 0:
                res = "late"
            else:
                raise Exception ("Unkown state of the temporal range [{0}-{1}]".format (self.start, self.end) )
            return res 

        def __repr__(self):
            return "State[{0}-{1}]".format ( self.start, self.end )
        
        def __str__(self):
            return "State:[{0}-{1}]".format ( self.start, self.end )

class TestState(unittest.TestCase):

    def test_state_future(self):
        start = datetime(2022, 12, 2, 10, 24, 34, 198130)
        end = datetime(2029, 12, 2, 10, 24, 34, 198130)
        result = State("activity-future", start, end).state()
        expected = "future"
        self.assertEqual( result, expected)

    def test_state_running(self):
        start = datetime(2019, 12, 2, 10, 24, 34, 198130)
        end = datetime(2029, 12, 2, 10, 24, 34, 198130)
        result = State("activity-running", start, end).state()
        expected = "running"
        self.assertEqual( result, expected)
    
    def test_state_late ( self ) :
        start = datetime(2019, 12, 2, 10, 24, 34, 198130)
        end = datetime(2019, 12, 5, 10, 24, 34, 198130)
        result = State("activity-late", start, end).state()
        expected = "late"
        self.assertEqual( result, expected)
