#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 01:04:19 2018
    Determines session length and number of document downloads for each session
    to the EDGAR system
    DEPENDENCIES:   input.py
                    output.py
                    exceptions.py
    INPUT:      inactivity_period.txt
                log.csv
    OUTPUT: sessionization.txt
            exception.txt      
@author: davidc
"""

import input_by_line as ibl
import output_by_line as obl
import error_n_except as ene
from datetime import datetime as dt
from datetime import timedelta as td

error_msg_incomplete = 'The record is incomplete'
error_msg_not_date = 'The date is incorrectly formatted'
error_msg_not_time = 'The time is incorrectly formatted'
time_date_format = '%Y-%m-%d %H:%M:%S'

one_more_line = True
max_lines = 1000
n = 1
user_ids = []
open_sessions = []

def format_datetime(day_00, time_00):
    ''' INPUT: two strings
        RETURNS: datetime object
    '''
    s = day_00 + ' ' + time_00
    return dt.strptime(s, time_date_format)

def calc_dt(bdate, btime, edate, etime):
    ''' INPUT: four strings: 
               beginning date & time, ending date & time
        RETURNS: difference between begin & end (seconds)
    '''
    begin = format_datetime(bdate, btime)
    end = format_datetime(edate, etime)
    diff = end - begin
    return diff.seconds + 1

def update_record(open_sessions, new_record):
    ''' Updates endtime, session time, trigger time
        Increments weblog count
        INPUT: new_record: records from current session
               open_sessions: records from open sessions
        RETURNS: open_sessions (new)
    '''
    idx = list(zip(*open_sessions))[0].index(new_record[0])
    open_sessions[idx][4] += 1      # increments webpage request count
    open_sessions[idx][2] = new_record[2]  # updates session end time
    # updates length of session in seconds
    btemp = open_sessions[idx][1]
    bdate, btime = btemp[:10], btemp[11:]
    etemp = open_sessions[idx][2]
    edate, etime = etemp[:10], etemp[11:]
    # updates session length (Seconds)
    open_sessions[idx][3] = calc_dt(bdate, btime, edate, etime)
    # updates trigger time
    open_sessions[idx][5] = format_datetime(edate, etime) + td(seconds=ip)
    return(open_sessions)

def format_weblog(rol):        
    ''' INPUT: None
        RETURNS: 
    '''
    delta_t = calc_dt(rol[1], rol[2], rol[1], rol[2])
    start_t = rol[1] + ' ' + rol[2]
    #trigger time: ttime is a time object
    ttime = format_datetime(rol[1], rol[2]) + td(seconds=ip)
    new_record = [rol[0], start_t, start_t, delta_t, 1, ttime]
    return new_record

def fetch_weblog():
    try:
       new_record = ibl.read_one_line(n)
    # catches the raised exception indicating end of file
    except TypeError:
       print('End of File')
       return False
    return new_record
        

# --- MAIN STARTS HERE ---
ip = ibl.inactivity_period()
while (one_more_line) and (n < max_lines):
    new_record = fetch_weblog()
    n += 1

    if ene.Is_Blank_Line(new_record): 
        continue
    if not new_record: 
        one_more_line = new_record
        break
    if not ene.Is_All_Fields_Here(new_record):
        obl.incomplete_record(error_msg_incomplete, new_record)
        continue
    if not ene.Is_Date_Format(new_record[1]):
        obl.not_date_format(error_msg_not_date, new_record)
        continue
    if not ene.Is_Time_Format(new_record[2]):
        obl.not_date_format(error_msg_not_time, new_record)
        continue
    
    formatted_record = format_weblog(new_record)
    # Updates open session or adds a new session
    if formatted_record[0] in user_ids:
        open_sessions = update_record(open_sessions, formatted_record)
    else:
        user_ids.append(formatted_record[0])
        open_sessions.append(formatted_record)
    # Checks if any other sessions have ended
    for ending_session in open_sessions:
        if ending_session[5] < dt.strptime(formatted_record[1], \
                                           "%Y-%m-%d %H:%M:%S"):
            obl.session_line(ending_session[:5])
            user_ids.remove(ending_session[0])
            open_sessions.remove(ending_session)       
for i in open_sessions:
     obl.session_line(i[:5])
print()
















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    