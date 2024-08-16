# if condition

'''n=int(input('enter a value'))
if n>100:
    print ('more than 100')'''




#if else condition
#wap to print the maximum number among given two numbers.
''''s=int(input('enter your value'))
p=int(input('enter your value'))

if s>p:
    print(s,' is max number')
else:
    print (p,' is max number')'''

#wap to find given number is even or odd 
'''n=int(input('enter value:'))
if n%2==0:
    print('even number')
else:
    print('odd number')'''

#wap to check given string is palindrome or not
'''s=input('enter value:')
if s== s[::-1]:
    print ('palindrom')
else:
    print('not a palindrom')'''

#wap to check given string are anagrams or not
'''s=input('enter value')
s1=input('enter a value')
if sorted(s)==sorted(s1):
    print('anagrams')
else:
    print('not a anagrams')'''

#wap to check given year is leep year on not

year=int(input('year:'))
if year%100!=0 and year%4==0:
    print('year is leap year')
else:
    print('not a leap year')
