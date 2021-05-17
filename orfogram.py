#!/usr/bin/env python3

import argparse
import mcb185
import random

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

# setup
parser = argparse.ArgumentParser(description='Explore orf length.')
# no required arguments, gives a standard number if you don't put in values

# optional arguments with default parameters
parser.add_argument('--size', required=False, type=int, default= 4500000,
	metavar='<int>', help='standard e.coli genome size [%(default)i]')
parser.add_argument('--min_orf', required=False, type=int, default=100,
	metavar='<int>', help='minimum orf size [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=0.5,
	metavar='<float>', help='gc fraction [%(default).3f]')
#switches
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
# finalization
arg = parser.parse_args()

#sets the seed of random to the same sequence (keeps seq the same) 
	#BUT you need to have --seed in terminal
if arg.seed: random.seed(1)
if arg.info: print(arg.size, arg.min_orf, arg.gc)


#generate rand genome of specified size, GC comp
seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)


#looking for ATG
lengths = []
for i in range(len(seq)-2):
	start = None
	stop = None
	if seq[i : i+3] == 'ATG':
		start = i
		for j in range(i, len(seq)-2, 3):
			codon = seq[j : j+3]
			if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				stop = j
				break
	if stop != None: 
		#print(start, stop)
		lengths.append((stop- start)/3) #how many AAs in ea ORF 
#print(lengths) #length of protein (3codons is 1 aa)
#lengths.sort()
#TURN VALUES INTO INT
lengths = [int(a) for a in lengths]
#print(lengths)

#counts number of genes produced
count = 0
for n in lengths:
	if n > arg.min_orf:
		count += 1			
#print(lengths)
print('number of genes produced:', count)

#histogram
histogram = [0] * (max(lengths) + 1)
for t in lengths: 
	histogram[t] += 1
print(histogram)

"""			
#making a histogram, only looking at the duplicated values, not all positions
for x in range(len(lengths)):
	dup = 0
	for y in range(len(lengths)):
		if lengths[x] == lengths[y]:
			dup += 1
		else:
			y += 1
	#only prints out the values that have the duplicates!
	#Issue: if lengths[x] is dup 6 times, you'll see it 6 times :(
	
	print(lengths[x], dup)
"""	

"""
worked and problem solved with Adrian


how many times did i see length x? 
how many counts at each length			
			
			
# terminal: python3 orfogram.py --info --seed --gc 0.45
"""

	




































