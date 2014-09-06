import sys

file=open('rosalind_rna.txt')

dnadata=file.read()
rnadata=''
for letter in dnadata:
	if letter=='T':
		letter='U'
	rnadata+=str(letter)

print rnadata