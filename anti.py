#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

rc_dna = ''

#range len-1 bc last len 0-12 not incl 12; 
# -1 to incl 0; -1 to go backwards 1 at a time

for i in range(len(dna)-1, -1, -1):
	nt = (dna[i])
	if 	 nt == 'A': rc_dna += 'T'
	elif nt == 'T': rc_dna	+= 'A'
	elif nt == 'C': rc_dna += 'G'
	elif nt == 'G':	rc_dna += 'C'
	else		  : rc_dna += 'n'

print(rc_dna)



"""

for i in range(len(dna)-1, -1, -1):
	nt = (dna[i])
	if 	 nt == 'A': nt = 'T'
	elif nt == 'T': nt = 'A'
	elif nt == 'C': nt = 'G'
	elif nt == 'G':	nt = 'C'
	else		  : nt = 'n'
	rc_dna +=nt
this would also work out because nt will only be changed during if statements


python3 anti.py
TTTTTTTTTTTCAGT
"""
