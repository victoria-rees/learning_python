#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here
import math

print(n) 

#running sum
s=0
for i in range(1, n + 1):
	s= s + i
print(s)

#factorial
fact=1
for i in range(1, n + 1):
	fact= fact * i
print(fact)

"""
#factorial from class
lnfac= 0.5 * math.log(math.tau) + (n+0.5) * math.log(n) \
	-n +1/(12*n)-1/(360*(n**3))
print(math.e**lnfac)
"""
"""
python3 sumfac.py
5 15 120
"""
