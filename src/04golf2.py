j,l=0,[]
for y in[len({*x.split()[:12]}&{*x.split()[13:]})for x in open(0)][::-1]:l+=[1+sum(l[len(l)-y:])];j+=2**y//2
print(j,sum(l))