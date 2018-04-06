#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:18:16 2018
    Contains two read functions for the EDGAR sessionization app
    INPUT:   inactivity_period.txt
             log.csv
    OUTPUT:  Data that is read from the respective file
@author: davidc
"""
import csv

#PATH = './../input/'             # Use when running from IDE
PATH = './input/'                 # Use when running from command line

default_inactivity_period = 2
testfile = 'log.csv'
inact_period = 'inactivity_period.txt'

def read_one_line(n):
    '''opens a csv file and reads one line
       Name of csv file is at top of input.py.
       CSV file contains a header.
       INPUT: a single integer indicating which line number to read
       RETURNS all elements as a list of strings
    '''
    with open(PATH + testfile, newline='') as f:
        reader = csv.reader(f)
        row_next = next(reader)
        for i in range(0,n):
            try:
                row_next = next(reader)
            except StopIteration:
                return False
    return row_next

def inactivity_period():
    '''opens a text file and reads a single integer
       txt file name is at top of input.py
       RETURNS an integer
    '''
    print(PATH + inact_period)
    with open (PATH + inact_period, newline='') as f:
        reader = csv.reader(f)
        nr = next(reader)
        try:
            ip = int(nr[0])
            if (ip < 0) or (ip > 86400):
                ip = default_inactivity_period
        except ValueError:
            if type(nr[0]) == 'float':
                ip = int(float(nr[0]))
            else:
                ip = default_inactivity_period
    return ip
















