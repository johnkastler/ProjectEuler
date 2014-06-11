#!/usr/bin/env python

import sys

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# 
# Step 1: figure out the fibonacci sequence up to 4,000,000,000
#

fibonacci = [1, 2]
max = 4000000000
z = len(fibonacci) - 1

while fibonacci[z] < max:
    x = len(fibonacci) - 1
    y = len(fibonacci) - 2
    fibonacci.append(fibonacci[x] + fibonacci[y])
    z = len(fibonacci) - 1

drop = len(fibonacci) - 1

# the last element in the array will be greater than what we want, so drop it
fibonacci = fibonacci[:drop]

#
# Step 2: let's find the even numbers and add them up
#

x = 0

for each in fibonacci:
    if not each % 2:
        x = x + each
        
print("the sum of all the even terms in the defined range is {0}".format(x))

