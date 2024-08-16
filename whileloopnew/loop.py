"""n=int(input('value'))
for row in range (1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()"""


"""l=[]
while True:
    value=int(input('enter n value:'))
    if value<0:
        break
    l.append(value)
print(l)"""

"""
c=int(input('value'))
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
    if c==pc:
        break
    n+=1"""

"""c=int(input())
ac=0
n=1
while True:
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==n:
       print(n)
       ac+=1
    if c==ac:
       break
    n+=1"""

c=int(input())
ac=0
n=1
while True:
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==n:
       ac+=1
    if c==ac:
        print(n)
        break
    n+=1