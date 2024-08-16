#wap to check how many integers are present in given string 

s=input()
c=0

for i in s:
    if i.isdigit():
        c+=1
print(c)



''' execution
take string input from user
creating vc variable with 0 as value because we are assuming that given string might be empty
taking string as anuj45686
iteration1: extract a from s and check the conditon if a in sring or not,
            a not in v, c become 0
iteration2: extract n from s and check the conditon if n in c or not,
            n not in v, c same 0
iteration3: extract u from s and check the conditon if u in c or not,
            u not in v, c same 0
iteration4: extract j from s and check the conditon if j in c or not,
            j not in v, c same 0
iteration5: extract 4 from s and check the conditon if 4 in c or not,
            4 in v, c become 1
iteration6: extract 5 from s and check the conditon if 5 in c or not,
            a in v, c become 2
iteration7: extract 6 from s and check the conditon if 6 in c or not,
            6 in v, c become 3
iteration8: extract 8 from s and check the conditon if 8 in c or not,
            8 in v, c become 4
iteration9: extract 6 from s and check the conditon if 6 in c or not,
            6 in v, c become 5

at last print c value 5'''