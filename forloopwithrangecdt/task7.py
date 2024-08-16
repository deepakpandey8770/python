#wap to find the sum of even digit present in odd index position.
s=input('value')
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==0:
            if ip%2!=0:
              sum +=k
print(sum)

'''executions
taking input from user
taking sum=0 bcz i am assuming that string is empty
taking string as 123456
iterations....
iteration1>> execute 1 from string from and check the  condition it is digit or not and it is digit check it is even or not
               so it not a even digit so sum=0
iteration2>> execute 2 from string from and check the condition it is digit or not and it is digit check it is even or not
                so it even digit present in odd index position so sum=2
iteration3>> execute 3 from string and check the condition it is digit or not and it is  digit check it is even or not
                so it is not a even digit so sum=2
iteration4>> execute 4 from string and check the condition it is digit or not and it is digit check it is even or not
               so it is even digit and present in odd index position so sum=6
iteration5>> execute 5 from string and check the conditon it is digit or not and it is digit check it is even or not
                so it not a even digit so sum=6
iteration6>> execute 6 from string and check the condition it is digit or not and it is digit check it is even or not
                so it is even digit and present in odd index position so sum=12

at last print the value of even number present in odd index position is 12
'''