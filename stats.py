#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
#print(sys.argv) #checking if my command line is in the list

#but we want list to be numbers, not string
s = []
for t in sys.argv[1:]:
	s.append(float(t)) #@position t along list, gets converted and added to a floating int
s.sort() #FOR ALL OF THEM, WE WANT TO ORGANIZE THE LIST!!
#print(s)

#count how many integers
count = 0
for i in range(len(s)):
	count += 1
print(count)

#what's the smallest #
print(min(s))
#also did print(s[0])

#what's the largest #
print(max(s))
#also did print(s[-1])

#mean- sum of numbers/Count
sum = 0
for i in range(len(s)):
	sum += s[i]
mean = sum/count
print('%.3f' %(mean))

#std dev- how far from the mean: ((#@position0 - mean)^2 =x) @all positions then get 
"""
loop for finding 'x' at all positions
get mean of all x = X and sqrt that

"""
x = 0 
for j in range(len(s)):
	x += (s[j] - mean) ** 2

y = math.sqrt(x/count)
print('%.3f' %(y))

#median- middle number of list
a = int(count/2)
b = int((count -1)/ 2)
med = (s[a] + s[b]) / 2
print('%.3f' %(med))



"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
