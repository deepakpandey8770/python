n=int(input())
pn=0
for i in range(1,n//2+1):
    if n %i==0:
        pn+=i
if n==pn:
    print('perfect number')
else:
    print('not a perfect')