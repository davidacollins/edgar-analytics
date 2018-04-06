# edgar-analytics
Simulates a continuous data stream identifying SEC document retrieval sessions on EDGAR

SUMMARIZATION APPROACH:
A single WHILE loop iterates through the data in the log.csv file, and does so one line at a time.  In keeping with the posted requirements, one line of data is read and processed before the next line of data is read.  As a trade-off between keeping the connection to the input file open and maximizing speed, the 'read file open' connection is closed once a single line is read.  Therefore, when the next line is read, all of the previous lines need to be reread to return to the appropriate place in the log.csv file.

Functions are grouped into modules by their utility: input, output, and error catching.  Given the small size of the application, the preprocessing files are kept in the main module.

NOTES:
- Sessionization.py has a hard limit of reading 1000 lines in log.csv as a redundant precaution against an infinite WHILE loop.  If you need to test with a larger log.csv file, then you will need to modify line 29 of sessionization.py.

- Damaged or incomplete data is handled by logging the damaged/incomplete record to a separate file: exceptions.txt, and descriptively identifying the problem.  This file, exceptions.txt, is produced when I run the tests in my directory structure, but is not produced when I run the tests in your directory structure.  Yet, all of the tests still pass in your directory structure.  Upon inspection of your run_tests.sh file, it appears that this occurs because the run_tests.sh file redirects outputs to a temp directory which compares the file contents to a static reference file in the respective output directory.  Thus the contents of the temp directory, including exceptions.txt, are not kept permanently.

- Datetime intervals are calculated using Python's internal Datetime Class which automatically handles time intervals spanning two days with a method to deliver the interval in seconds.  Therefore explicit calculations are not included in these scripts.
