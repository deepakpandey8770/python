#wap to print inndex postion of vowels in a given strings 
s=input('value:')
v='aeiouAEIOU'
for ip in range(len(s)):
    k=s[ip]
    if k in v:
        print(ip)

'''executions
taking input from user
taking vowels as'aeiouAEIOU'
taking string as  hello
iterations....
itetation1>> execute h from given string and check the condition it is in v or not 
             so h not in v ip=non
iteration2>> execute e from given string and check the conditon it is in v or not
            so e in v so ip=1
iteration3>> execute l from given string and check the condition it is in v or not
            so l not in v so ip=1
iteration4>>  execute l from given string and check the condition it is in v or not
            so l not in v so ip=1
iteration5>> execute o from given string and check the condition it is in v or not
            so o in v so the ip is 1 and 4

at last print the value of ip is=1,4

'''