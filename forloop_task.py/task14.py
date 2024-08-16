#wap to print the sum of 1st N number
n=int(input("value"))
c=0
for i in range(1,n+1):
    c+=i
print(c)
'''execution
taking n=input from user 
taking c=0  i am assuming that given value is 0
taking integer as 3
iterations:
iteration1: extract 3 from n and adding in c so c become 
           c=3
iteration2: extract 2 from n and adding in c so c become 
            c=5
iteration3: extract 1 from n and adding in c so c become 
            c=6

at last print the value of c
so sum of fast n number is 6

'''