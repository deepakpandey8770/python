#wap to find the sum of odd digit present in even index positon.
s=input('value')
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2!=0:
            if ip%2==0:
                sum+=k
print(sum)

'''execution
taking input from user 
taking sum=0 bcz i am assuming that given string is empty
taking string as 2416387
iterations.....
iteration1>> execute 2 from string and check the condition it is digit or not and it is digit so check it is odd digit or not
            so it is even digit so suum=0
iteration2>> execute 4 from string and check the conditon it is digit or not and it is digit so check it is odd digit or not
            so it is even digit so sum=0
iteration3>> execute 1 from string and check the conditon it is digit or not and it is digit so check it is odd digit or not
            so it is odd digit so check index position is even or not so ip is even so sum=1
iteration4>> execute 6 from string and check the conditon it is digit or not and it is digit so check it is odd digit or not
            so it is even digit so sum=1
iteration5>> execute 3 from string and check the condition it is digit or not and it is digit so check it is odd digit or not
            so it is odd digit so check index position is even or not so ip is even so sum=4
iteration6>> execute 8 from string and check the conditon it is digit or not and it is digit so check it is odd digit or not
            so it is even digit so sum=4
iteration7>> execute 7 from string and check the condition it  is digit  or not and it is digit so check it is odd digit or not
            so it odd digit  so check index position is even or not so ip is even so sum=11

at last print the value of  sum of odd digit present in even index position is 11



'''