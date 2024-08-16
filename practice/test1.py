def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return 
        else:
            return True
def reverse(num):
    rev=0
    dummy=num
    while dummy>0:
        rem=dummy%10
        dummy//=10
        rev=rev*10+rem
    return rev
def ispaliprime(n):
    rev=reverse(n)
    if n==rev and isprime(n):
        return True
    else:
        return False
def paliprime(ll,ul):
    for n in range(ll,ul+1):
        if ispaliprime(n):
            print(n)
paliprime(1,100)