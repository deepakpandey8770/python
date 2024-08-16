"""n1=int(input('value:'))
n2=int(input('value:'))
if n1> n2:
    print(n1,'n1 is greater')
else:
    print(n2,'n2 is greater')"""

"""n1=input('value:')
if n1==n1[::-1]:
    print(n1,'is palindrome')
else:
    print(n1,'not a palindrome')
"""


"""s=input('value')
s1=input('value')
if sorted (s) == sorted (s1):
    print (s ,s1,'is a anagram')
else :
    print (s,s1,'not a anagram')"""
"""
s=int(input('value'))
if s%2==0:
    print(s,'even number')
else:
    print(s,'is odd number')"""




"""
n=int(input('value'))
n1=int(input('value'))
n2=int(input('value'))
if n==n1==n2:
    print('no one greater')
elif n>n1 and n>n2:
    print(n,'is greater than')
elif  n1>n2:
    print(n1,'is greater ')
else:
    print(n2,'is greater')"""



"""n=int(input('value'))
n1=int(input('value'))
n2=int(input('value'))
n3=int(input('value'))
if n==n1==n2==n3:
    print('no one greater')
elif n>n1 and n>n2 and n>n3:
    print (n,'is greater')
elif n1>n2 and n1>n3:
    print (n1,'is greater')
elif n2>n3:
    print(n2,'is greater')
else:
    print(n3,'is greater')"""



"""w1=int(input('value:'))
w2=int(input('value:'))
w3=int(input('value:'))
w4=int(input('value:'))
w5=int(input('value:'))
if w1==w2==w3==w4==w5:
    print('no one is greater')

elif w1>w3 and w1>w3 and w1>w4 and w1>w5:
    print(w1,'w1 is greater')
elif w2>w3 and w2>w3 and w2>w4 and w2>w5:
    print(w2,'w2 is greater')
elif w3>w4 and w3>w5:
    print(w3,'w3 is grater')
elif w4>w5:
    print(w4,'w4 ia  grater')
else:
    print(w5,'w5 is grater')"""



""""
n1=int(input('value:'))
n2=int(input('value:'))
n3=int(input('value:'))

if n1>n2:
    print(n1,'is greater')
    if n1>n3:
        print(n1,'is greater')
    else:
        print(n3,'is greater')
else:
    if n2>n3:
        print(n2,'is greater')
    else:
        print(n3,'is greater')"""


    
"""a=int(input('value'))
b=int(input('value'))
c=int(input('value'))
d=int(input('value'))

if a>b:
    print(a,'is greater')
    if a>c:
        print(a,'is greater')
        if a>d:
            print(a,'is greater')
        else:
            print(d,'is greater')
    else:
        if c>d:
            print(c,'is greater')
        else:
            print(d,'is greater')
else:
    if b>c:
        print(b,'is greater')
        if b>d:
            print(b,'is greater')
        else:
            print(d,'is greater')
    else:
        if c>d:
            print(c,'is max')
        else:
            print(d,'is max')"""



"""a=int(input('value:'))
b=int(input('value'))
c=int(input('value'))
d=int(input('value'))
e=int(input('value'))
        
if  a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a,'is max')
            else:
                print(e,'is max')
        else:
            if d>e:
                print(d,'is max')
            else:
                print(e,'is max')
    else:
        if c>d:
            if c>e:
                print(c,'is max')
            else:
                print(e,'is max')
        else:
            if d>e:
                print(d,'is max')
            else:
                print(e,'is max')
else:
    if b>c:
        if b>d:
            if b>e:
                print(b,'is max')
            else:
                print(e,'is max')
        else:
            if d>e:
                print(d,'is max')
            else:
                print(e,'is max')
    else:
        if c>d:
            if c>e:
                print(c,'is max')
            else:
                print(e,'is max')
        else:
            if d>e:
                print(d,'is max')
            else:
                print(e,'is max')
        """
    
"""s={'hello',True}
s1=()
for i in s:
   print(i)"""
"""
#wap to check how many element are present in given string without using length function.
s=input('value')
c=0
for i in s:
    print('enter for loop')
    c+=1
print(c)"""


"""#wap to check how many times sub string is present in given string without using count method;
s=input('value')
sub=input('value')
c=0
for i in s:
    if i==sub:
        c+=1
print(c)
"""
"""#wap to check how many vowels are present in given string
s=input('value')
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c+=1
print(c)"""


"""
s=input('value')
sub=input('value')
c=0
for i in s:
    if i == sub:
        c+=1
print(c)"""


"""s=input('value:')
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c+=1
print(c)"""


"""
#wap to check how many consonent are present in given string.
s=input('value')
v='aeiouAEIOU'
c=0
for i in s:
    if i not in v:
        c+=1
print(c)"""

#wap to check how many vowels and how many consonent are present in given string

"""s=input("enter value: ")
v='aeiouAEIOU'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(vc)
print(cc)"""

"""#wap to check how many integers are present in given string

s=input('value:')
c=0
for i in s:
    if  i . isdigit():
        c+=1
print(c)"""


"""#wap to print sum of integer present in given string
s=input('value')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)
"""

"""s=input('value')
v='aeiouAEIOU'
c=0
for i in s:
    if i not in  v:
        c+=1
print(c)"""
"""
#wap to print sum of integer present in given string

s=input('value')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)"""

"""#wap to print the sum of even digit present in a given string.
s=input('value')
sum=0
for i in s:
    if i.isdigit():
         k=int(i)
         if k%2==0:
             sum+=k
print(sum)"""

"""s=input('value')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            sum+=k
print(sum)"""
"""
s=input('value')
even=0
odd=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            even+=k
        else:
            odd+=k
print(abs(even-odd))"""

"""#wap to print how many special character  are present in given string
s=input('value')
sc=0
for i in s:
    if not i.isalnum():
        sc+=1
      
print(sc)
"""