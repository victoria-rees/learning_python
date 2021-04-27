#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
import math

# ---------------
#assign command line values to variables:


val = []
for i in sys.argv[1:]:
	val.append(int(i))
#print(cov) #checked to see if val was right

g_siz = val[0]	# chr len
r_num = val[1]	# num reads
r_len = val[2]	# how long read is
#print(g_siz, r_num, r_len) #checking to see if assigned to correct num
# --------------
"""
coverage is total bases generated/size of genome

1st we need to create another list, fill w random 
"""
c_bp = 0	#counting the 
for j in range(r_num):
	bp = [] #for each num of reads, we have a new bp list
	for k in range(g_siz):
		bp.append(random.randint(0, r_len-1)) #adds random number of len
		
#print(bp)
"""
for m in range(len(bp)):
	x = bp[m] / g_siz

	print(x)

"""
#report min coverage
print('The minimum coverage is: ' )
print(min(bp))

#report max coverage
print('The maximum coverage is: ')
print(max(bp))

#report avg coverage
	#count of bp generated		
c_bp = 0
for a in range(len(bp)):
	c_bp += 1

print('The average coverage is: ')
sum = 0
for z in range(1,len(bp)-1):
	sum += bp[z]
print(sum/c_bp)	


"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
