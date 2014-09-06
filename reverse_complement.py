import sys

file=open('rosalind_revc.txt')

dnadata=file.read()
rc=''
for letter in dnadata:
	if letter=='T':
		letter='A'
	elif letter=='A':
		letter='T'
	elif letter=='C':
		letter='G'
	elif letter=='G':
		letter='C'
	rc+=str(letter)

for i in reversed(rc):
	sys.stdout.write(i)