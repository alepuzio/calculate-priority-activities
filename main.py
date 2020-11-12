# -*- coding: utf-8 -*-
"""Module main
@overview entry point of the application
"""

from src.group_importance import GroupImportance
from src.group_time import GroupTime
from src.group_activity import GroupActivity
from src.group_priority import GroupPriority

from src.final_csv import FinalCSV
from src.source_csv import SourceCSV 


if __name__ == '__main__':
 
    #log start elaboration
    FinalCSV(".\\", "ordered-activities.csv", GroupPriority( GroupActivity(SourceCSV(".\\", "activity-date.csv", GroupTime()).file()) ) .sort( SourceCSV(".\\", "activity-importance.csv", GroupImportance()).file() )).file()
    #log end elaboration
    


