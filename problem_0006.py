#!/usr/bin/env python

from math import pow

"""
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

bottomofRange = 1
topOfRange = 100

topOfRange = topOfRange + 1

def sumOfSquares(x, y):
    holder = 0
    for n in range(x, y):
        thisPow = pow(n, 2)
        holder = holder + thisPow
    return(holder)

def squareOfSums(x, y):
    holder = 0
    for n in range(x, y):
        holder = holder + n
    return(pow(holder, 2))

def diffOfValues(x, y):
    value = x - y
    return(value)

print(diffOfValues(squareOfSums(bottomofRange, topOfRange), sumOfSquares(bottomofRange, topOfRange)))