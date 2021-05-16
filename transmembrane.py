#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein *
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa (N-terminus)
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa (C-terminus)



#hydrophobicity score function:
def kd(seq):
	hydro = 0
	for aa in seq:
		if   aa == 'I' : hydro += 4.5
		elif aa == 'V' : hydro += 4.2
		elif aa == 'L' : hydro += 3.8
		elif aa == 'F' : hydro += 2.8
		elif aa == 'C' : hydro += 2.5
		elif aa == 'M' : hydro += 1.9
		elif aa == 'A' : hydro += 1.8
		elif aa == 'G' : hydro -= 0.4
		elif aa == 'T' : hydro -= 0.7
		elif aa == 'S' : hydro -= 0.8
		elif aa == 'W' : hydro -= 0.9
		elif aa == 'Y' : hydro -= 1.3
		elif aa == 'P' : hydro -= 1.6
		elif aa == 'H' : hydro -= 3.2
		elif aa == 'K' : hydro -= 3.9
		elif aa == 'R' : hydro -= 4.5
		elif aa == 'E' : hydro -= 3.5 
		elif aa == 'Q' : hydro -= 3.5 
		elif aa == 'D' : hydro -= 3.5 
		elif aa == 'N' : hydro -= 3.5 	#initially had an else 
	return hydro/len(seq)
	
def alpha(seq, w, h): #window and kd values(h) of signal or hydroph regions
	for i in range(len(seq) - w + 1):
		if kd(seq[i:i+w]) > h and seq[i:i+w] != 'P':
			return True
	return False
		#using bullions to signify if region is or is not transmembrane.

#gets all the sequences; reads fasta file (from classwork)
ids = []
proteins = []
with open(sys.argv[1]) as fp:
	seq = []
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			words = line.split() #splits line by spaces
			ids.append(words[0][1:]) #words[0] gives first word,
						#[1:] gives you that word from character 1 onwards
			if len(seq) > 0 : proteins.append(''.join(seq))
			seq = []
		else:
			seq.append(line)
	proteins.append(''.join(seq)) #adds last straggler
#print(len(ids), len(proteins)) #showing we have all 


#only print the id of the proteins that are transmembrane!!
for id,seq in zip(ids, proteins):
	sig = seq[:30] #sig for first 30 aas
	hyd = seq[30:] #hydro region after 30 aas
	#only a transmembrane protein if alpha = true for signal AND hydroph regions
	if alpha(sig, 8, 2.5) and alpha(hyd, 11, 2): #conditions from lines 13/14
		print(ids)
			
"""
assisted by adrian and Haley. initially had an else statement to combine E/Q/D/N
but that may impact values due to * being a stop codon and not on the list for AAs
"""	






















"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
