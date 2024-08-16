"""LL=int(input())
UL=int(input())
n=LL
while n<=UL:
    sum=0
    i=2
    while i<=n//2:
        if n%i==0:
            sum+=i
        i+=1
    if n==sum:
        print(n)
n+=1


s=input('value')
se=0
so=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            se+=k
        else:
            if k%2!=0:
                so+=k
print(abs(se-so))

    """

"""#how many special character are present in given string
s=input('value')
sc=0
for i in s:
    if not i.isalnum():
        sc+=1
print (sc)"""

"""s=eval(input('value'))
sum=0
for i in s:
    sum+=i
print(sum)"""
"""s=eval(input('value'))
se=0
so=0
for i in s:
    if i%2==0:
        se+=i
    else:
        if i%2!=0:
         so+=i
print(abs(se-so))
"""
"""ll=int(input('value'))
sum=0
for i in range(ll,ll+1):
    sum+=i
print(sum)"""


"""s=int(input('value'))
dummy=s
sum=0
l=len(str(s))
while dummy > 0 :
    rem=dummy%10
    dummy//=10
    sum+=rem**l

if s==sum:
    print('armstorng')
else:
    print('not a armstrong')"""

"""n=input('value')
se=0
so=0
for i in n:
    k=int(i)
    if k%2==0:
        se+=k
    else:
        so+=k
print(abs(se-so))"""
"""
n=input('value')
sc=0
for i in n:
    if not i.isalnum():
        sc+=1
print(sc)"""


"""s=eval(input('value'))
se=0
so=0
for i in s:
    if i%2==0:
        se+=i
    else:
            so+=i
print(se-so)"""

"""n=int(input())
pn=0
for i in range(1,n//2+1):
    if n %i==0:
        pn+=i
if n==pn:
    print('perfect number')
else:
    print('not a perfect')"""
"""s=input('value')
sub=input('value')
c=0
for i in s:
    if i in sub:
        c+=1
print(c)"""

"""s=input('value')
v='aeiou'
c=0
for i in s:
    if i in v:
        c+=1
print(c)"""
"""
s=input('value')
v='aieou'
vc=0
cc=0
for i  in s:
    if i in v:
        vc+=1
    else:
        cc+=1
print(vc,cc)
"""

s=input('value')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)