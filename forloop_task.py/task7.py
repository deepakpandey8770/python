#wap to print sum of integer present in given string.
s=input('value')
si=0
for k in s:
    if k.isdigit():
        k=int(k)
        si+=k
print(si)

''' execution.
takeing  string inputs from user
creating si variable with s,0 as value because we are assuming that given string might be empty
taking stirng as 1234

iteration:extracting 1 from string and check 1 is digit or not and it is digit so convert it into integer
             so 1 is digit ,so 1 is add in si =1
iteration2: extracting 2 from string and check 2 is digit or not and it is digit so convert it into integer
             so 2 is digit ,so 1 is add in si =3
iteration3:  extracting3 from string and check 3 is digit or not and it is digit so convert it into integer
             so 3 is digit ,so 3 is add in si =6
iteration4:  extracting 4 from string and check 4 is digit or not and it is digit so convert it into integer
             so 4 is digit ,so 4 is add in si = 10

at last print c=10'''

