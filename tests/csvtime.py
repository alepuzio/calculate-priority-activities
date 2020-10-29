# -*- coding: utf-8 -*-
"""Module timeActivity
Object about the management of the data about the project and time
"""
from datetime import date
from datetime import datetime
from personalLogging import PersonalLogging
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

