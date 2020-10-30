import unittest
from datetime import date
from datetime import datetime
from personalLogging import PersonalLogging

class State:

        """
        It calculate the state of an activity
        """
        def __init__(self, newStartDate, newEndDate):
            self.start = newStartDate
            self.end = newEndDate
            self.log = PersonalLogging()

        def state(self):
            res = None
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  
            self.log.warning("State", "state","today:{0}".format( str ( type (today ) ))) 
            self.log.warning("State", "state", "self.start:{0}".format ( str ( type ( self.start ) )   ))
            if today < self.start:
                res = "future"
            elif self.start < today and today < self.end:
                res = "running"
            elif self.end < today:
                res = "late"
            else:
                raise Exception ("Unkown state of the temporal range [{0}-{1}]".format (self.start, self.end) )
            return res 


class TestState(unittest.TestCase):

    def test_state_ok(self):
        start = datetime(2019, 12, 2, 10, 24, 34, 198130)
        end = datetime(2029, 12, 2, 10, 24, 34, 198130)
        result = State(start, end).state()
        expected = "running"
        self.assertEqual( result, expected)

