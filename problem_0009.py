#!/usr/bin/env python

from math import pow
from sys import exit

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a = 1
b = 2
c = 3

aMax = 332
bMax = 499
cMax = 997

while True:
	value = a + b + c
	print("checking {0} + {1} + {2} = {3}".format(a, b, c, value))
	while value > 1000:
		# decrement  a, check
		# decrement  b, check
		# decrement  c, check
		if value == 1000:
			print("the answer is {0} {1} {2}".format(a, b, c))
			if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
				print("the answer is {0} {1} {2}".format(a, b, c))
				exit(0)
	a = a + 1
	b = b + 1
	c = c + 1
	
"""
what do we know
	c cannot be greater than 998
	b cannot be greater than 499
	a cannot be greater than 332

find valid Pythagoreans such that a does not exceed aMax

def findAllMatches():
	while a <= aMax and b <= bMax and c <= cMax:
"""