#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 03:34:47 2018
    Contains two output functions for the EDGAR sessionization app
    Writes to text files: 
                          sessionization.txt
                          exceptions.txt
    INPUT:  The formatted output record
             
@author: davidc
"""

#PATH = './../output/'            # Use when running from IDE
PATH = './output/'                # Use when running from command line
output_file = 'sessionization.txt'
exceptions_file = 'exceptions.txt'

def write_list(session_list, f):
    i = 0
    for s in session_list:
        f.write(s)
        if i != (len(session_list) - 1):
            f.write(',')
        i += 1    

def session_line(session_list):
    session_list[3] = str(session_list[3])
    session_list[4] = str(session_list[4])
    with open(PATH + output_file, 'a') as f:
        write_list(session_list, f)
        f.write('\n')

def incomplete_record(error_msg_incomplete, new_record):
    with open(PATH + exceptions_file, 'a') as f:
        f.write(error_msg_incomplete + '\n')
        write_list(new_record, f)
        f.write('\n')

def not_date_format(error_date_format, new_record):
    with open(PATH + exceptions_file, 'a') as f:
        f.write(error_date_format + '\n')
        write_list(new_record, f)
        f.write('\n')

def not_time_format(error_time_format, new_record):
    with open(PATH + exceptions_file, 'a') as f:
        f.write(error_time_format + '\n')
        write_list(new_record, f)
        f.write('\n')
