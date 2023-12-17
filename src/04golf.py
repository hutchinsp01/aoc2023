a,b=0,[]
for l in[*open(0)][::-1]:s=38-len({*l.split()});b+=[1+sum(b[len(b)-s:])];a+=2**s//2
print(a,sum(b))