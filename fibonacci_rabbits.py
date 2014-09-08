r = []
sum=0
n=29
k=5

def f(x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        return r[x-1]*(k+1)-k*(r[x-1]-r[x-2])

i=0
while i<n:
    r.append(f(i))
    i+=1

j=1
for seq in r:
    print j,
    print seq
    j+=1