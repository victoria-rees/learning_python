#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

# your code goes here

"""
print(dna)
print(dna[:3])
print ('attempt1')


a=0
for c in dna:
	a += 3
	print(dna[:a])
print ('attempt 2')
#keeps adding 3 on top of previous iteration
"""

#step sizes over 0 and length of dna length
#printing dna from i=0 to i+3 and then moves from i=3 to i=6 etc!!
for i in range(0, len(dna), 3):
	print ( dna[i:i+3] )



"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
