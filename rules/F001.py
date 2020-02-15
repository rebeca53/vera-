#!/usr/bin/env python
"""F001.py: Rule Source files should not use the '\r' (CR) character"""
__author__ = "Rebeca N R"
__copyright__ = "Copyright 2020, SA Project"

__license__ = "MIT"

import vera
message = "Source files should not use the '\r' (CR) character"
for fileName in vera.getSourceFileNames():
    if (fileName == "-"):
        # cant check the content from stdin
        continue

    file = open(fileName, "r") #open file
    lineNumber = 1
    for line in file: #go line by line
        if line.endswith('\r'): # if a '\r' found isolated (no valid char before and after)
            vera.report(fileName, lineNumber, message) # report fileName linecounter message
        lineNumber = lineNumber + 1
    file.close() #close file