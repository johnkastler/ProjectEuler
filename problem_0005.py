#!/usr/bin/env python

import sys

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

checkValue = 20

# y will continue to increment until we find our winner
#y = 208000000
y = 1

while True:
    #print("checking for {0} against {1}".format(checkValue, y))
    
    # reset x each time
    x = 1
    
    # our winner will have incremented counter up to 20 with each successful check
    counter = 0
    
    while x <= checkValue:
        if not y % x:
            counter = counter + 1
        
        x = x + 1
    
    if counter == checkValue:
        print("The answer is {0}".format(y))
        sys.exit(0)
        
    y = y + 1