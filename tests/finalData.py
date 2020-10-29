# -*- coding: utf-8 -*-
"""Module priority
Object about the management of the data about the project and priority
"""
import unittest
#from period import Late
#from period import ToStart
from period import Running


class Priority:
    def __init__(self, newTimeActivity, newImportance):
        self.date = newTimeActivity
        self.importance = newImportance

    def activity(self):
        """
        @return the name of the Activity
        """
        return self.importance.activity()
        
    def points(self):
        """
        @return the points of the Activity
        """
        return int(self.importance.importance()) * int(self.date.days())
        
     
    def __str__(self):
        return "Priority:{0}".format(self.name() ) 
    
    def __repr__(self):
        return "Priority[{0}]-[{1}]".format(self.name() , str (  self.importance.importance() ) )
        
class TestPriority(unittest.TestCase):

    def test_points(self):
        priority = Priority( TimeActivity ( date ), importance) 
        result = priority.points()
        expected = 10
        self.assertEqual(result, expected)

class CSV:

    def __init__(self, newPriority):
        self.priority = newPriority

    def activity(self):
        return self.priority.activity()
        
    def points(self):
        return self.priority.points()

    def __str__(self):
        return "CSV:{0}".format(self.name() ) 
    
    def __repr__(self):
        return "CSV[{0}]-[{1}]".format(self.name() ,  self.points() ) 


class GroupPriority:    
    def __init__(self, newListPriority):
        self.listPriority = newListPriority
    
    def __str__(self):
        return "GroupPriority:{0}".format(str( self.listPriority ) )
    
    def __repr__(self):
        return "GroupPriority[{0}]\n>[{1}]".format( len ( self.listPriority ), self.listPriority)

    def sort(self, listImportance):
        """
        sort the list of Priority objects in order ascent of number of days and importance
        """
        return self.union(listImportance)

    def union (self, listImportance):
        """
        join the data of the attribute list and the list of activities with their importance
        """
        result = []
        for i in range ( len ( listImportance )  ) :
            date = self.listPriority.rows()[i]
            importance = listImportance[i]
            if date.action() == importance.activity():
                #result.append ( CSV(Priority( ToStart ( Late ( Running ( date ) ) ), importance) ))
                result.append ( CSV ( Priority ( Running ( date ) , importance) ) )
            else:
                raise Exception("Different project in row {0}:{1}-{2};".format( str(i) , date.action(), importance.activity() ) )
        return GroupPriority(result)        
    
    def rows(self):
        """
        @return the list of activities with thir dates
        """
        return self.listPriority
