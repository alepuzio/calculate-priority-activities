import unittest
from datetime import date
from datetime import datetime
from src.personal_logging import PersonalLogging
from tests.numberdays import NumberDays

class State:

        """
        It calculate the state of an activity
        """
        def __init__(self, newNumberDays):
            self.numberDays = newNumberDays
            self.log = PersonalLogging()

        def activity(self):
            return self.numberDays.name

        def state(self):
            res = None
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  #TODO centralize ina classe
            #TODO centralize logic or use decorator
            if self.numberDays.running(today) :#running
                res = "running"
            elif self.numberDays.future(today):#future
                res = "future"
            elif self.numberDays.late(today): #late
                res = "late"
            else:
                raise Exception ("Unkown state of the temporal range [{0}]".format (self.numberDays) )
            return res 

        def __repr__(self):
            return "State({0})".format ( self.numberDays )
        
        def __str__(self):
            return "State: {0}".format ( self.numberDays )



class TestState(unittest.TestCase):

    def test_state_future(self):
        start = datetime ( 2022, 12, 2, 10, 24, 34, 198130 )
        end = datetime ( 2029, 12, 2, 10, 24, 34, 198130 ) 
        result = State ( NumberDays( "activity-future", start, end ) ).state()
        expected = "future"
        self.assertEqual( result, expected ) 

    def test_state_running(self):
        start = datetime ( 2019, 12, 2, 10, 24, 34, 198130 )
        end = datetime ( 2029, 12, 2, 10, 24, 34, 198130 )
        result = State ( NumberDays ( "activity-running", start, end ) ) .state()
        expected = "running"
        self.assertEqual( result, expected )
    
    def test_state_late ( self ) :
        start = datetime ( 2019, 12, 2, 10, 24, 34, 198130 )
        end = datetime ( 2019, 12, 5, 10, 24, 34, 198130 ) 
        result = State ( NumberDays ( "activity-late", start, end  ) ).state()
        expected = "late"
        self.assertEqual( result, expected)
