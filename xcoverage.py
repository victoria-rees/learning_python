#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random


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
bp = [0 for j in range(g_siz)]

for j in range(r_num):
	a = random.randint(0, g_siz - r_len) 
	b = a + r_len
	for k in range(a, b):
		bp[k] += 1
		
min = bp[r_len]
max = bp[r_len]
tot = 0

for l in bp[r_len : -r_len]:
	if l < min : min = l
	if l > max : max = l
	tot += l
	
print(min, max, tot/(g_siz - 2*r_len))
"""	
entirely helped by Adrian, he explained why it works this way as well.

"""
"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
