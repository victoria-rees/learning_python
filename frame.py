#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'


for i in range(len(dna)):
	
	print(i, i%3 , dna[i])		
				
	
print()


"""
	#for frame in range(3):
		#or position in range(frame, len(dna)-2,3):
			#codon = dna[position:position+3]
	#if f == 0 : f = 0
for frame in range (3):
	#print (f'reading frame {frame+1}', end =' ')
	for position in range(frame, len(dna)-2, 3):
		codon= dna[position:position+3]
		print(f'in frame{frame+1}')
	
for frame in range(3):
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		if codon == 'ATG':
			print(f'start codon at {position} in frame {frame+1}')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			print(f'stop codon at {position} in frame {frame+1}')
"""
"""
python3 frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
