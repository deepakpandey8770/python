n=int(input('value'))
for i in range(2,n//2+1):
    if n%i==0:
        print('not a prime')
    else:
        print('prime number')