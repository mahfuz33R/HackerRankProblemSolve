#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if "AM" in s:
        if s[:2] == "12":
            s = re.sub(s[:2], "00", s)
            s = re.sub("AM", "", s)
        else:
            s = re.sub("AM", "", s)
        return s
    if "PM" in s:
        if s[:2] == "12":
            se = re.sub("PM", "", s)
        else:
            hour = int(s[:2])
            hour += 12
            ho = str(hour)
            new = re.sub(s[:2], ho, s)
            se = re.sub("PM", "", new)
        
        return se
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
