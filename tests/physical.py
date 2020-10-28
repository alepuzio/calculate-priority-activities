# -*- coding: utf-8 -*-
"""Module physical
Object and method about the I/O operations
"""

import csv
import os
from personalLogging import PersonalLogging

class SourceCSV:
    def __init__(self, newPath, newFilename, newGroupTime):
        self.filename = newFilename
        self.path = newPath
        self.groupTime = newGroupTime
        self.log = PersonalLogging()

    def file(self):
        """
        read the data from the file
        """
        result = []
        completePath =  CompletePath(self.path, self.filename)
        if completePath.existing() :
            with open(completePath.path(), newline = '') as csvfile:
                result = self.groupTime.rows ( csv.DictReader ( csvfile ) )
        else:
            raise Exception ("The file [{0}] is not present, I stop the elaboration ".format (  completePath.path()    )       )
        self.log.info( "Elaborated file: {0}".format(  completePath.path() ) )
        return result

class CompletePath:#TODO create decorator cache
    def __init__(self, new_partialPath, new_filename):
        self.filename = new_filename
        self.partialPath = new_partialPath
        self.log = PersonalLogging()

    def existing(self):
        """
        @return true if the path exists already in the hard disk
        """
        return os.path.exists( self.path () )

    def path(self):
        """
        @return complete path (withfilename) of the file
        """
        return "{0}{1}{2}".format(self.partialPath, os.sep , self.filename)

"""'
class TestCompletePath(unittest.TestCase): dependent on os, then it's not a unit test
class TestCompletePath(unittest.TestCase): dependent by the OS, not unit test
class TestFinalCSV(unittest.TestCase): dependent by the OS, not unit test
"""


class FinalCSV:

    def __init__(self, new_path, new_filename, newGroupPriority):
        self.filename = new_filename
        self.path = new_path
        self.groupPriority = newGroupPriority
        self.log = PersonalLogging()


    def file(self):
        """
        write the final file
        """
        result = []
        completePath =  CompletePath(self.path, self.filename) 
        with open(completePath.path(), 'w', newline='') as csvfile:
            fieldnames = ['Activity', 'Points']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for i in range ( len( self.groupPriority.rows() ) ):
                tmp = self.groupPriority.rows()[i]
                self.log.info ( "data {0},{1}".format( tmp.activity(),  tmp.points() ) )
                writer.writerow({'Activity': tmp.activity(), 'Points': tmp.points()})
        self.log.info("Elaborated file: {0}".format( completePath.path() )     )
 
class Safe:
    def __init__(self, newFinalCSV):
        self.finalCSV = newFinalCSV

    def file(self):
        """
        if the file already exists, it block the execution and saves original file
        """
        completePath =  CompletePath(self.path, self.filename) 
        if completePath.existing():
            raise Exception ("The file [{0}] exists already, I stop the elaboration and I don't write".format ( completePath.path() ) )
        else:
            self.finalCSV.file()
