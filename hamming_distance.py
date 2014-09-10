def hamming_distance(s1,s2):
	distance=0
	for idx in range(0,len(s1)-1):
		#print "index: %s, s1: %s, s2: %s" % (idx, s1[idx], s2[idx])
		if s1[idx]!=s2[idx]:
			distance+=1
	return distance

file=open('hamming.txt')

dnadata={}
id=0
for line in file:
	dnadata[id]=line
	id+=1

print hamming_distance(dnadata[0],dnadata[1])
