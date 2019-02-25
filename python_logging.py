"""
Helpful link for logging basics
https://docs.python.org/2/library/string.html
https://docs.python.org/2.0/ref/strings.html
https://docs.python.org/2/howto/logging.html
https://docs.python.org/2/library/logging.html#logrecord-attributes

Python Logging Lvls : DEBUG < INFO < WARNING < ERROR < CRITICAL
"""

#! /usr/bin/env/ python

import logging
import datetime
import time


# Get actual time and properly format it into strings
actual_time = datetime.datetime.now()
#str_date_time = actual_time.strftime("%Y-%m-%d %H:%M:%S")
str_date = actual_time.strftime("%Y-%m-%d")

# String format of our logs
# Formatter,used bellow , uses %(<dictionary key>)s styled string substitution; the possible keys are documented in LogRecord attributes.
log_format = "%(asctime)s\t%(name)s\t%(levelname)s\t\t%(message)s"

# Create logger object
logger = logging.getLogger("LOGTEST")
logging.basicConfig(format=log_format, filename=str_date) # Pass the filename and the log strings format used in file logs
logger.setLevel(logging.DEBUG)                            # Set logging level to display debug and higher level in the file

# Create console handler to display log on the console and not just in file
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)                   # Can select a different logging lvl for the console if needed

# Create formatter for the console handler
formatter = logging.Formatter(log_format)                 # Can select a different log strings format for the console if needed

# Add the formatter to console handler
console_handler.setFormatter(formatter)

# Add the console handler to logger
logger.addHandler(console_handler)

# How to implement it your code
logger.debug("This is a simple debug message")
logger.info("This is a simple informative message")
logger.warning("This is a message to remember that you have to be careful over here")
logger.error("This message is to let you know that something went wrong")
logger.critical("This message is to let you know that you f*ck up really bad!")
