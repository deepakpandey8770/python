def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return  True
    else:
        return False
'''def check_prime(n):
    summ=0
    while n>0:
        rem=n%10
        n//=10
        if isPrime(rem):
            summ+=rem
    print('The given number prime numbers summis',summ)
    if isPrime(summ):
        return True
    else:
       return False
print(check_prime(9502512004))         
'''

def isEven(n):
    if n%2==0:
        return True
    else:

        return False

def checking_evenNumbers(n):
    summ=0
    while n>0:
        rem=n%10
        n//=10
        if isEven(rem):
            summ+=rem
    print(summ)
    if isPrime(summ):
        return True
    else:
        return ('false')
print(checking_evenNumbers(6281723225))
