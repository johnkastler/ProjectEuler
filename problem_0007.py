#!/usr/bin/env python

from sys import exit

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number? 104743
"""

checkPoint = 10001

primes = []
x = 2

def checkForPrime(x):
	holder = 0
	for n in range(2, x):
		if not x % n:
			holder = holder + 1
	if holder == 0:
		primes.append(x)
		
def checkArrayLength(x):
	if len(x) == checkPoint:
		print(x)
		print(x[-1:])
		exit(0)

while True:
	checkForPrime(x)
	checkArrayLength(primes)
	print(len(primes))
	x = x + 1