#wap to find the sum of integers present in a given string
s=input('value')
sum=0
for  ip in range(len(s)):
    if s[ip].isdigit():
        sum+=int(s[ip])
print(sum)

'''execution
taking input from user 
taking sum=0  bcz i am assuming that the sum of given  number is 0
taking input as h1i2p34
iterations...
iteration1>> execute h from string and check the condition it is digit or not
            so h is not digit so sum=0
iteration2>> execute 1 from string and check the condition it is digit or not
            so 1 is a digit so sum=1
iteration3>> execute i from string and check the condition it is  digit or not
            so i is not a digit so sum remain same=1
iteration4>> execute 2 from string and check the conditionn it is  digit or not 
            so it is digit so sum =3
iteration 5>> execute p from string and check the condition it is digit or not
            so it is not a digit so sum ramain same=3
iteration6>> execute 3 from string and check the condition it is digit or not 
            so it is digit so sum=6
iteration7>> execute 4 from string and check  the condition it is digit or not
            so it is digit so sum =10

            
at last print the value of sum=10

'''