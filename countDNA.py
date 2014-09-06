import sys

file=open('rosalind_dna.txt')

dnadata=file.read()

dna={'A':0, 'C':0, 'G':0, 'T':0, '\n':0}
for letter in dnadata:
	dna[letter]+=1
del dna['\n']
print(dna['A']),
print(dna['C']),
print(dna['G']),
print(dna['T']),