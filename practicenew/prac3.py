"""s='hello'
sum=''
for i in s:
    print(i)"""
"""l=[11,22,33,44]
for i in l:
    print(i)"""
"""#wap to check how many element are present in given string without using length function.
s=input('enter a value')
c=0
for i in s:
    c+=1
print(c)"""

"""#wap to check how many  times sub string is present in the given string without using count method.
s=input('enter a value')
sub=input('enter a value')
c=0
for i in s:
    if i == sub:
        c+=1
print(c)
    """

"""#wap to print how many vowels are present in given string.
s=input('value')
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c+=1
print(c)"""

"""#wap to check how many consonent are present in given string 
s=input('value')
v='aeiou'
c=0
for i in s:
    if i not in v:
        c+=1
print(c)"""

"""#wap to check how many consonent and how many vowels are present in given string
s=input('value')
v='aeiou'
vc=0
cc=0
for i in s:
    if i in v:
        vc+=1
    else:
        cc+=1
print(vc)
print(cc)"""

"""#wap to check how many integers are present in given string 
s=input('value')
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)"""

"""#wap to print sum of integer present in given string
s=input('value')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)"""

"""#wap to print sum of even number present in given stirng
s=input('value')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            sum+=k
print(sum)"""

"""#wap to print absolute difference between sum of even and odd digit present in a given string
s=input('value')
sum=0
odd=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            sum+=k
        else:
            if k%2!=0:
                odd+=k
print(abs(sum-odd))"""
            
"""#wap to print how many special characters are present in given string
s=input('value')
c=0
for i in s:
    if not  i.isalnum():
        c+=1
print(c)
"""

#wap to find the sum of digit of a given list without using sum function 

l=eval(input('value'))
sum=0
for i in l:
    sum+=i
print(sum)