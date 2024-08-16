#wap to print even or not
'''
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
#print(iseven(20))
#wap to check even or not in given range by using functions
def evennumber(ll,ul):
    for i in range(ll,ul+1):
        if iseven(i):
            print(i)
evennumber(1,20)
#wap to check prime number in given range by using funcitons
def isprime(n):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    return False
            else:
                return True
def primenumber(ll,ul):
    for n in range(ll,ul+1):
        if isprime(n):
            print(n)
primenumber(1,30)


#wap to check  pali prime in given range by using functions
def isprime(n):
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

def ispaliprime(n):
    rev=reverse(n)
    if n==rev and  isprime(n):
        return True
    else:
        return False
def paliprime(ll,ul):
    for n in range(ll,ul+1):
        if ispaliprime(n):
            print(n)
paliprime(1,100)


#wap to print emirp number in given range by using functions

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
        '''
"""
#wap to print special number in given range by using functions
def isspecial(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(2,rem+1):
            fact*=i
        summ+=fact
    if summ == n:
        return True
    else:
        return False
      
def specialnumber(ll,ul):
    for n in range(ll,ul+1):
        if isspecial(n):
            print(n)
specialnumber(1,100)

"""
#wap to print armstrong number in given range by using functions
def isarmstrong(n):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if summ==n:
        return True
    else: 
        return False
def armstrong(ll,ul):
    for n in range(ll,ul+1):
        if isarmstrong(n):
            print(n)
armstrong(1,100

)