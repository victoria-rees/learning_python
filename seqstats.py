#!/usr/bin/env python3

import argparse
import mcb185
import statistics

#-----arg stuff----
# setup
parser = argparse.ArgumentParser(description='Stats about sequence.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required fasta file')
# finalization
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file):
	#print(name, len(seq))
	length.append(len(seq))
length.sort()
print(length)
#min
print('min:', length[0])
#print(min(length))

#max
print('max:', length[-1])
#print(max(length))
"""
#total length
sum = 0
for value in length:
	sum += value
print(sum)
"""

#another way to get sum:
print(sum(length))

#average
print('mean:', statistics.mean(length))
#median
print('median:', statistics.median(length))
#n50
print(mcb185.n50(length)) 
#prints none??

"""
runsum = 0
for value in length:
	runsum += value
	if runsum > sum/2 : 
		print('n50 is', value)
		break
"""


# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length-- sum values, once value is greater than half the total, 
	#we report that one
# Use argparse
# Make useful functions and add them to your library

