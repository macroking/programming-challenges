from __future__ import print_function
import os
import sys
from datetime import datetime
from datetime import timedelta

def dayOfProgrammer(year):
    days = sum([ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    total = 0
    if year >= 1700 and year <= 1917:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            total = days + 1
        else:
            total = days
    if year == 1981:
        total = days - 13
    if year >= 1919:
        if year % 4 == 0:
            total = days + 1
        else:
            total = days
    sd = datetime(year, 1, 1)
    print(sd, year)
    return sd + timedelta(days = 256)


if __name__ == '__main__':
    f = open('./hackerrank/input.txt')
    year = int(f.readline().strip())
    result = dayOfProgrammer(year)
    print(result)
