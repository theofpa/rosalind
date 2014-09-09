import sys
file=open('gc-content.fas')

def getcontent(dnastring):
	dnadict={'A':0, 'C':0, 'G':0, 'T':0}
	for letter in dnastring:
		dnadict[letter]+=1
	return ((dnadict['C']+dnadict['G'])*1.0/sum(dnadict.values()))*100

dnadata={}
for line in file:
	if line.startswith('>'):
		id=line[1:-1]
		dnadata[id]=''
	else:
		dnadata[id]+=str(line[:-1])

max=0

for id in dnadata:
	newmax=getcontent(dnadata[id])
	if(newmax>max):
		max=newmax
		maxid=id

print maxid
print max