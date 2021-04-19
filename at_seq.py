#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

bp = 30
seq = ''
at = 0
t = 0.6

for i in range(bp):
	r = random.random()
	if r < t:
		if random.random() < 0.5: 
			seq += 'A'
			at += 1
		else: 
			seq += 'T'
			at += 1
	else: 
		seq += random.choice('GC')
	
print(bp, at/bp, seq)

"""
#keeping random.seed(1) gives a consistent 0.5; without, it varies and reaches 0.6
for i in range(bp):
	nt = random.choice('AAACCGGTTT') #using random.choice
	seq += nt
print(seq)

for i in range(bp):
	r = random.random()
	if r < t:
		seq += random.choice('AT')
		at += 1
	else: 
		seq += random.choice('GC')	
print(seq, at)


python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
