#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

## Notes:

A Prime Number can be divided evenly only by 1 or itself.
And it must be a whole number greater than 1.

"""

factors = []
primes = []

def factor(x):
	y = 1
	while y <= x:
		if not x % y:
			factors.append(y)
		y = y + 1

def prime(x):
	for each in x:
		counter = 0
		y = 1
		while y <= each:
			if not each % y:
				counter = counter + 1
			y = y + 1
		if counter < 3:
			primes.append(each)
	print("The largest prime is {0}".format(primes[-1:]))

				
factor(600851475143)
prime(factors)