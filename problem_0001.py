#!/usr/bin/env python

print("""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

question (math related): what about numbers that are a multiple of both? e.g. 15
question (python related): what are the "best practices" for this solution?
""")

# initialize the empty arrays
threesList = []
fivesList = []

# determine if a number is a multiple
def multiples(x, list):
    for y in range(0,1000):
        if not y % x:
            list.append(y)

# sum up the list of multiples
def addThem(list):
    mysum = 0
    for each in list:
        mysum = mysum + each
    return(mysum)

multiples(3, threesList)
multiples(5, fivesList)

print(' - the mutiples of 3 are: {0} {1}'.format(threesList,'\n'))
print(' - the mutiples of 5 are: {0} {1}'.format(fivesList,'\n'))
print(' - all the threes add up to {0} {1}'.format(addThem(threesList),'\n'))
print(' - all the fives add up to {0} {1}'.format(addThem(fivesList),'\n'))
print(' - the grand total is {0} {1}'.format(addThem(threesList) + addThem(fivesList),'\n'))