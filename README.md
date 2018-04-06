# edgar-analytics
Simulates a continuous data stream identifying SEC document retrieval sessions on EDGAR

Sessionization.py has a hard limit of reading 1000 lines in log.csv as a redundant precaution against an infinite WHILE loop.

Damaged or incomplete data is handled by logging the damaged/incomplete record to a separate file: exceptions.txt, and descriptively identifying the problem.  This file, exceptions.txt, is produced when I run the tests in my directory structure, but is not produced when I run the tests in your directory structure.  Yet, all of the tests still pass in your directory structure.

Datetime intervals are calculated using Python's internal Datetime Class which automatically handles time intervals spanning two days with a method to deliver the interval in seconds.  Therefore explicit calculations are not included in these scripts.
