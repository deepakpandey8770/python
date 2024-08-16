#wap to find the sum of even digit present in odd index position
s=input('value')
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==0:
            if ip%2!=0:
                sum+=k
print(sum)

'''executions
taking input from user
taking sum=0 bcz i am assuming that there is empty string
taking input as 12a4b6
iterations....
iteration1>> execute 1 from string and check the condition it is even or not 
            so  it  is not even number so sum=0
iteration2>> execute 2 from sring and check the condition it is even or not
            so it  is even number and ip is odd  sum=2
iteration3>> execute a from string and check the condition it is digit or not
            so it is not a digit so sum=2
iteration4>> execute 4 from string and check the conditionn it is even or not
            so it is digit and even number and ip is odd so sum=6
iteration5>> execute b from string and check the conditon it is digit or not 
            so it not a digit so sum=6
iteration6>> execute 6 from string and check the condition it is digit or not
            so it is digit and it is even digit  present in odd index positon so sum=12

at last print the value of sum of even number present in odd index position  is 12

'''