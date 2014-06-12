#!/usr/bin/env python

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def findLargestPal(x, y):
    
    # create placeholder
    largestPal = 0
    
    # we need to remember what y is even after we increment it
    initialY = y
    
    # let the ugly nesting begin! (how can this be made better?)
    # also, there must be a better way than hardcoding 1000 here, maybe an $(x * 10) type thing?
    while x < 1000:
        while y < 1000:
            
            # Do I really need to convert the product to a string?
            n = str(x * y)
            
            # two things I don't like about this:
            # 1) the nesting is specific to a number of no more than 6 digits and
            # 2) there's got to be a better way than nesting like this
            if n[0:1] == n[-1:]:
                if n[1:2] == n[-2:-1]:
                    if n[2:3] == n[-3:-2]:
                        
                        # need to make z an int again for numerical comparison
                        if largestPal < int(n):
                            largestPal = int(n)
                            
            y = y + 1
        
        # reset y so we can process the next iteration of x
        y = initialY
        x = x + 1
        
    print("the larget palindrome is {0}".format(largestPal))

findLargestPal(100, 100)