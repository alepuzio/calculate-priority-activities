# -*- coding: utf-8 -*-
"""Module main
@overview entry point of the application
"""

from groupimportance import GroupImportance
from grouptime import GroupTime
from groupactivity import GroupActivity
from grouppriority import GroupPriority

from finalcsv import FinalCSV
from sourcecsv import SourceCSV 


if __name__ == '__main__':
 
    #log start elaboration
    FinalCSV(".\\", "ordered-activities.csv", GroupPriority( GroupActivity(SourceCSV(".\\", "activity-date.csv", GroupTime()).file()) ) .sort( SourceCSV(".\\", "activity-importance.csv", GroupImportance()).file() )).file()
    #log end elaboration
    


