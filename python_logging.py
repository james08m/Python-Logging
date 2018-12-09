"""
Helpful link ti logging basics
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


actual_time = datetime.datetime.now()
str_date_time = actual_time.strftime("%Y-%m-%d %H:%M:%S")
str_date = actual_time.strftime("%Y-%m-%d")
log_format = "%(asctime)s\t%(name)s\t%(levelname)s\t\t%(message)s" # formatter string uses %(<dictionary key>)s styled string substitution; the possible keys are documented in LogRecord attributes.

# Create logger object
logger = logging.getLogger("LOGTEST")
logging.basicConfig(format=log_format, filename=str_date) # Pass file name and custom log format for the file
logger.setLevel(logging.DEBUG)                            # Set level to display debug and high level message

# Create console handler to display log on console and not just on file
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)                   # Can select a different lvl for the console if needed

# create formatter
formatter = logging.Formatter(log_format)                 # Can select a different format for the console if needed

# add formatter to ch
console_handler.setFormatter(formatter)

# add ch to logger
logger.addHandler(console_handler)

# 'application' code
logger.debug("This is a simple debug message")
logger.info("This is a simple informative message")
logger.warning("This is a message to remember that you have to be careful over here")
logger.error("This message is to let you know that something went wrong")
logger.critical("This message is to let you know that you f*ck up really bad!")

time.sleep(10)
