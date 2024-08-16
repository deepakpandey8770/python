#wap to find the sum of index position of digit in a given string 
s=input('value')
si=0
for ip in range(len(s)):
    if s[ip].isdigit():
        si+=ip
print(si)

'''executions
taking input from user
taking si=0 bcz i am assuming that string is empty
taking string as 1s2d3f5
iterations....
iteration1>> execute 1 from string and check the condition it is digit or not
            so it is digit so si=0
iteration2>> execute s from string and check the condition it is digit or not
            so it is not digit so si=0
iteration3>> execute 2 from string and check the condition it is digit or not
            so it is digit so si=2
iteration4>> execute d from string and check the condition it is digit or not
            so it is not a  digit so si=2
iteration5>> execute 3 from string and check the conditionn it is digit or not
            so it is digit so si=6
iteration6>> execute f from string and check the condition it is digit or not
            so it is not a digit so si=6
iteration7>> execute 5 from string and check the condition it is digit or not
            so it is digit so si=12

at last print the sum of index position is 12

'''