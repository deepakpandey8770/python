#wap to find the sum of index position of substring in a given string..
s=input('value:')
sub=input('value:')
c=0
for ip  in range(len(s)):
    if s[ip:ip+len(sub):]==sub:
        c+=ip
print(c)

'''executions
taking string input from user
taking substring input from user
taking c=0 bcz i am assuming that given string is empty
taking string as deepak
taking sub string as p

iterations....
iteration1>> execute d from string and check the condition it is in sub or not
             so it is not in sub so c=0
iteration2>> execute e from string and check the condition it is in sub or not
            so it is not in sub so c=0
iteration3>> execute e from string and check the condition it is in sub or not
            so it is not in sub so c=0
iteration4>> execute p from string and check the condition it is in sub or not
            so it is in sub so c=3
iteration5>> execute a from sring and check the condition it is in sub or not
            so it is not in sub so c ramain same
iteration6>> execute k from string and check the condition it is in sub or not
            so it in not in sub so c remain same c=3

at last print the index postion of substring is 3

'''