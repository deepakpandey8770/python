#wap to check how  many times the given substring present in given string
s=input('value')
sub=input('value')
c=0
for ip in range(len(s)):
    if s[ip:ip+len(sub):]==sub:
        c+=1
   # print(s[ip:ip+len(sub):])
print(c)

'''executions  
taking string input from user 
taking sub string input from user
taking c=0 bcz i am assuming that string is empty
taking string as deepak
taking substring as e

iterations....
iteration1>> execute d from string and check the condition it is in sub or not 
             so d not in sub so c ramain same c=0
iteration2>> execute e from string and check the condition it is in sub or not
             so e in sub so c=1
iteration3>> execute e from string and check the condition it is in sub or not
             so e in sub so c=2
iteration4>> execute p from string and check thee condtion it is in sub or not
            so p not in sub so c=2
iteration5>> execute a from string and check the condition it is in sub or not
            so a not in sub so c=2
iteration6>> execute k from string and check the condition it is in sub or not
            so k not in sub so c=2

at last print the value of c=2
'''