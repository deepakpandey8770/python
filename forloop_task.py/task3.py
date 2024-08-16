#wap to check how many consonent  are present in given string
s=input()
v ='aeiouAEIOU'
c=0

for i in s:
    if i.isalpha() and i not in v:
        c+=1
print(c)

''' execution
take string input from user
take another input as vowel and value is 'aeiouAEIOU'
creating c variable with 0 as value because we are assuming that given string might be empty 
taking string as harshad
iteration1: extract h from s and check the conditon if h in v or not,
            h not in v, c become 1
iteration2: extract a from s and check the conditon if a in v or not,
            a  in v, c become same 1
iteration3: extract r from s and check the conditon if r in v or not,
            r not in v, c become 2
iteration4: extract s from s and check the conditon if s in v or not,
             s not in v, c become 3
iteration5: extract h from s and check the conditon if h in v or not,
            h not in v, c is become 4
iteration6: extract a from s and check the conditon if a in v or not,
            a in v, c is remain same 4
iteration7: extract d from s and check the conditon if d in v or not,
            d not in v, c is become 5



at last print c value is 5
'''