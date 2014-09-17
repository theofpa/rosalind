import sys
file=open('cons-dataset.fas')

dnadata={}
for line in file:
	if line.startswith('>'):
		id=line[1:-1]
		dnadata[id]=''
	else:
		dnadata[id]+=str(line[:-1])

s=len(dnadata.itervalues().next())
dna={'A':[0]*s, 'C':[0]*s, 'G':[0]*s, 'T':[0]*s}
for i in range(0,s):
	for j in dnadata:
		#print dnadata[j][i],
		dna[dnadata[j][i]][i]+=1
	#print



max=0

for i in range(0,s):
	for id in dna:
		newmax=dna[id][i]
		if(newmax>max):
			max=newmax
			maxid=id
	max=0
	sys.stdout.write(maxid)
print

for nuc,num in dna.iteritems():
	print nuc+":",
	for i in dna[nuc]:
		print i,
	print
