"""def addition():
    return 10+25
print(addition())"""
"""def addition ():
    return 10+25
additionresult=addition()
print(additionresult)"""

"""def iseven(n):
    if n%2==0:
        return True
    else:
        return False
def evennumber(ll,ul):
    for n in range(ll,ul+1):
        if iseven(n):
            print(n)
evennumber(1,30)
"""
"""def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
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
def ispali(n):
    rev=reverse(n)
    if n==rev and isprime(n):
        return True
    else:
        return False
def paliprime(ll,ul):
    for n in range(ll,ul+1):
        if ispali(n):
            print(n)
paliprime(1,1000)"""
"""def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
def reverse(num):
    rev=0
    dummmy=num
    while dummmy>0:
        rem=dummmy%10
        dummmy//=10
        rev=rev*10+rem
    return True
def isemirp(n):
    rev=reverse(n)
    if n==rev and isprime(n) and isprime(rev):
        return True
    else:
        return False
def emirpnumber(ll,ul):
    for n in range(ll,ul+1):
        if isemirp(n):
            print(n)
emirpnumber(1,1000)
"""

def isspecial(n):
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(2,rem+1):
            fact*=i
        summ+=fact
    if summ==n:
        return True
    else:
        return False
    
def special(ll,ul):
    for n in range(ll,ul+1):
        if isspecial(n):
            print(n)
special(1,200000)