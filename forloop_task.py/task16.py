'''wap to check the given number is perfect number or not.

when a number is equalto sum of its divisor then we can called as a perfect number.
'''
n=int(input('value'))
pn=0
for i in range(1,n//2+1):
    if n%i==0:
        pn+=i
if n==pn:
    print(n,'is perfect number')
else:
    print(n,'is not a perfect number')

'''exectuion
taking input from user
taking pn=0 because i am assuming that given input is 0
taking input as 6
iteration:
iteration1: extract 1 from n and checking the condition and reminder is  0
            so the pn=1
iteration2: extract 2 from n and checking the condition and reminder is 0
            so the pn=3
iteration3 : extract 3 from n and checking the condition and reminder is 0
            so the pn=6

            
at last print the perfect number is 6



'''