import argparse
import math
import mcb185
import os

"""
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking ?? switch look at seed in orfogram!
# The program should output a FASTA file (but with Ns or lowercase)

## Complexity Filter ##

Make a program that inputs genomic sequence and outputs a masked version of the
sequence where low-complexity regions are replaced either with an ambiguity
character (N for nt, X for aa) or lowercase. Your program should work with
either nucleotide or amino acid sequence and have separate default thresholds
for each. The output should allow for lowercase, N, or X, as appropriate. It
should also report the sequence as a FASTA file in 80 column width.

break down "idiot proof"- file empty, letters that are not incl in lists
	tell them they dumb
	- 
command lines:
python3 --fasta Data/aa_prot.fa 
python3 --fasta Data/nt_prot.fa --nt
python3 --fasta Data/datadump.py

"""

# setup argparse to enter in seq file/window size/threshold
parser = argparse.ArgumentParser(description='Complexity Filter.')
# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='input a sequence file')

parser.add_argument('--w', required=False, type=int, default=10,
	metavar='<int>', help='window for complexity (AA) [%(default)i]')

parser.add_argument('--t1', required=False, type=float, default=1.0,
	metavar='<float>', help='default threshold for nts [%(default).3f]')
parser.add_argument('--t2', required=False, type=float, default=2.5,
	metavar='<float>', help='default threshold for AAs [%(default).3f]')
#switch default aa and nt 
parser.add_argument('--nt', action='store_true',
	help='on= you are inputing a nt seq, off = file has AA seq')
parser.add_argument('--lc', action='store_true',
	help='on= receive output with lowercase, off = receive output with N or X')
# finalization
arg = parser.parse_args()

#making sure input file is fasta, not empty, and correct
filesize = os.path.getsize(arg.fasta)
if filesize == 0:
	print("This file is empty")
	exit()
	
#read the fasta file in AAs- check if first line has >
if arg.fasta.endswith('.fa'):
	for name, seq in mcb185.read_fasta(arg.fasta): #making sure it's fa file
		seq = seq.upper() #makes all letters upper if they have lower  in their file
		print(f'>{name}')
else: 
	print("wrong file type, did not provide a fasta file")
	exit()

def entropy(probs):
	assert(math.isclose(sum(probs), 1.0))
	h = 0 
	for p in probs:
		if p != 0: h -= p * math.log2(p)
	return h
	
def nt_seq_entropy(seq):
	A = 0
	T = 0
	C = 0
	G = 0
	total = 0
	for nt in seq:
		total += 1
		if	 nt == 'A' : A += 1
		elif nt == 'T' : T += 1
		elif nt == 'C' : C += 1
		elif nt == 'G' : G += 1
		else : total -= 1
	if total != 0:
		A /= total
		T /= total
		C /= total
		G /= total
		return entropy((A, T, C, G))
	else :
		return 0
	

def aa_seq_entropy(seq):
	A = 0
	C = 0
	D = 0
	E = 0
	F = 0
	G = 0
	H = 0
	I = 0
	K = 0
	L = 0
	M = 0
	N = 0
	P = 0
	Q = 0
	R = 0
	S = 0
	T = 0
	V = 0
	W = 0
	Y = 0
	tot = 0
	for aa in seq:
		tot += 1
		if 	 aa == 'A' : A += 1
		elif aa == 'C' : C += 1
		elif aa == 'D' : D += 1
		elif aa == 'E' : E += 1
		elif aa == 'F' : F += 1
		elif aa == 'G' : G += 1
		elif aa == 'H' : H += 1
		elif aa == 'I' : I += 1
		elif aa == 'K' : K += 1
		elif aa == 'L' : L += 1
		elif aa == 'M' : M += 1
		elif aa == 'N' : N += 1
		elif aa == 'P' : P += 1
		elif aa == 'Q' : Q += 1
		elif aa == 'R' : R += 1
		elif aa == 'S' : S += 1
		elif aa == 'T' : T += 1
		elif aa == 'V' : V += 1
		elif aa == 'W' : W += 1
		elif aa == 'Y' : Y += 1
		else : tot -= 1
	if tot != 0:
		A /= tot
		C /= tot
		D /= tot
		E /= tot
		F /= tot
		G /= tot
		H /= tot
		I /= tot
		K /= tot
		L /= tot
		M /= tot
		N /= tot
		P /= tot
		Q /= tot
		R /= tot
		S /= tot
		T /= tot
		V /= tot
		W /= tot
		Y /= tot
		return entropy((A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y))
	else :
		return 0

#seq = 'MKLMMMMMMMGPPPKLTTTGTTTHIIIKRRRRRRRRRRRRRR'
#not_aa = ['B', 'J', 'O', 'U', 'X', 'Z']

#looking through protein
out = ''
w = arg.w
t1 = arg.t1 #nt
t2 = arg.t2 #aa

t = None
r = None
f = None #new! store funct in variable!!

if arg.nt:
	t = arg.t1
	r = 'N'
	f = nt_seq_entropy
else:
	t = arg.t2
	r = 'X'
	f = aa_seq_entropy
	
for i in range(len(seq)-w + 1):
	wind = seq [i : i+w]
	h = f(wind)
	if h >= t : out += seq[i]
	elif arg.lc : out += seq[i].lower()
	else: 		  out += r #if user didn't put lc, they want N
print(out)



"""
Final project collaboration with Adrian
still needed- fool proof if aa contains letters not in aa code- print that
			- fool proof if person turned on switch for nt but its aa 
			- fool proof if person leaves switch off but it IS nt.
"""






