#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:27:03 2018
    Catches errors and exceptions
    INPUT:  A line from the csv file
    OUTPUT: Indicator variable showing 
            if the error has been triggered (boolean)
@author: davidc
"""

from datetime import datetime as dt

date_format = '%Y-%m-%d'
time_format = '%H:%M:%S'

def Is_Blank_Line(rol):
    #if (type(rol) == "<class 'list'>") and (len(rol) == 0):
    try:
        if len(rol) == 0:
            return True
        else:
            return False
    except TypeError:
        return False

def Is_All_Fields_Here(rol):
    if len(rol) >=6:
        return True
    else:
        return False
    
def Is_Date_Format(dd):
    try:
        dt.strptime(dd, date_format)
        return True
    except:
        return False

def Is_Time_Format(tt):
    try:
        dt.strptime(tt, time_format)
        return True
    except:
        return False
