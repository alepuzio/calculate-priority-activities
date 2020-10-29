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
    


