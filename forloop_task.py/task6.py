#wap to check how many times sub string is present in the given string
s=input('enter value:')
sub=input('enter value:')
c=0

for i in s:
    if  i==sub:
        c+=1
print(c)

''' execution
take string input from user
take another input as sub string
creating c variable with 0 as value because we are assuming that given string might be empty 
taking string as animesh
taking sub stiring as m
iteration1: extract a from s and check the conditon if a in sub or not,
            a not in sub, c become 0
iteration2: extract n from s and check the conditon if n in sub or not,
            n not in sub, c become 0
iteration3: extract i from s and check the conditon if i in sub or not,
            i not in sub, c become 0
iteration4: extract m from s and check the conditon if m in sub or not,
            m in sub, c become 1
iteration5: extract e from s and check the conditon if e in sub or not,
            e not in sub, c is same 1
iteration6: extract s from s and check the conditon if s in sub or not,
            s not in sub, c is same 1
iteration7: extract h from s and check the conditon if h in sub or not,
            h not in sub, c is same 1

            at last print c value is 1
'''