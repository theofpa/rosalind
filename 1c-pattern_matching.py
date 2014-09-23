import re
s='GATATATGCATATACTT'
t='ATAT'

for i in re.finditer('(?='+t+')',s):
	print i.start(),