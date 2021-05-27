import random



def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

#gc content
def gc(dna):
	g = dna.count('G')
	c = dna.count('C')
	return (g + c)/len(dna)

#n50
def n50(length):
	length.sort()
	runsum = 0
	total = sum(length)
	for value in length:
		runsum += value
		if runsum > total/2 : 
			print('n50:', value)
			break
"""
#n50 as a while loop
def n50(length)
	length.sort()
	runsum = 0
	total = sum(length)
	i = 0
	while runsum < total/2:
		runsum += length[i]
		i += 1
	return length[i]
"""

#create rand seq of rand length
def randseq(length, gc):
	seq = ''
	for i in range(length):
		if random.random() < gc:
			seq += random.choice('GC')
		else:
			seq += random.choice('AT')
	return seq


#translation dictionary!!
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

#translates sequence
def translate(seq):
	seq = seq.upper() #ensures sequence is uppercase
	protein = ''
	for i in range(0, len(seq)-2, 3): #goes thru seq in 3 steps
		codon = seq[i:i+3]
		aa = gcode[codon]
		#protein += aa or I could say protein += gcode[seq[i:i+3]] instead of lines 91-92
		if codon in gcode:
			protein += aa #is codon in dictionary?
		else:
			protein += 'X' #if not, print X
	return protein


#storing the ORF LENGTH	
def orf(seq):
	length = []
	for i in range(len(seq)-2):
		start = None
		stop = None
		if seq[i:i+3] == 'ATG':
			start = i
			for j in range(i, len(seq)-2, 3):
				codon = seq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					stop = j
					break
		if stop != None:
			length.append((stop-start)/3) #number AAs in our orf	
	return length

#reverse compliment
def rev_comp(seq):
	rc_seq = ''
	for i in range(len(seq)-1, -1, -1):
		nt = (seq[i])
		if	 nt == 'A' : rc_seq += 'T'
		elif nt == 'T' : rc_seq += 'A'
		elif nt == 'C' : rc_seq += 'G'
		elif nt == 'G' : rc_seq += 'C'
		else		   : rc_seq += 'n'
	return rc_seq

#longest_orf
def longest_orf(seq):
	assert(len(seq)>0)
	#find the start codon!
	atg = []
	for i in range(len(seq)-2):
		if seq[i:i+3] == 'ATG' : atg.append(i)
		max_length = 0
		max_seq = None
	for beg in atg:
		stop = None
		for j in range(beg, len(seq)-2, 3):
			codon = seq[j:j+3]
			if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				stop = j
				break
		if stop != None:
			code_len = stop - beg + 3
			if code_len > max_length:
				max_length = code_len
				max_seq = seq[beg:beg + code_len]
	if max_seq == None: return None
	return translate(max_seq)



















