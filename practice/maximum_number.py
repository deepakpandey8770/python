a=int(input('value:'))
b=int(input('value:'))
c=int(input('value:'))
d=int(input('value:'))
e=int(input('value:'))
if a==b==c==d==e:
    print('no one maximum')
if a>b and a>c and a>d and a>e:
    print('a is maximum')
elif b>c and b>d and b>e:
    print('b is maximum')
elif c>d and c>e:
    print('c is maximum')
elif d>e:
    print('d is maximum')
else:
    print('e is maximum')
