#wap to print the index position of consonent in given string..
s=input('value:')
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] .isalpha(): 
        if s[ip] not in v:
            print(ip,s[ip])

'''executions
taking input from user
taking v='aeiouAEIOU'
taking stirng as hello

iterations.......
iteration>> execute h from s and check the condition it is in v or not
            so h not in v so ip=0
iteration2>> execute e from s and check the condition it is in v or not
            so e in v so ip ramain same
iteration3>> execute l from s and check the condiotion it is in v or not 
            so l not in v so ip=0,2
itetation4>> execute l from s and check the condition it is in v or not 
             so l not in v so ip=0,2,3
iteration 5>> execute o from s and check the condition it is in v or not
            so o in v so ip ramain same ip=0,2,3
at last print the ip and s[ip]
 so     ip=0,2,3
 and s[ip]=h l l


'''