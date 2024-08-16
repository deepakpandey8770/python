#wap to find the sum of even number present in even index position..
s=input('value')
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==0:
            if ip%2==0:
                sum+=k
print(sum)


'''execution
taking input from user
taking sum=0 bcz i am assuming that given string is empty
taking string as 1123456
iterations...
iteration1>> execute 1 from string and check the condition it is digit or not and it is digit so check it is even or not
                so it not a even number so sum=0
iteration2>> execute 1 from string and check the conditon it is digit or not and it is digit so check it is even or not 
                so it not a even number so sum=0
iteration3>> execute 2 from string and check the conditon it is digit or not and it is digit so check it is even or not
                so it even number so sum=2
iteration4>> execute 3 from string and check the conditon it is digit or not and it is digit so check it is even or not
                so it not a even number so sum remain  same 
iteration5>> execute 4 from string and check the condition it is digit or not and it is digit so check it is even or not
                so it even number so sum =6
iteration6>> execute 5 from string and check the conditon it is digit or not and it is digit so  check it is even or not
                so it not a even number so sum ramain same
iteration7>> execute 6 from string and check the condition it is digit or not and it is digit so check  it is even or not
                so it even number so sum =12

at last print the value of sum of even index position is 12

'''