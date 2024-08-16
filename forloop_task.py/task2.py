#wap to print how many vowel are present in given string..

s=input ()
v='aeiouAEIOU'
c=0

for i in s:
    if i in v:
        c+=1
print(c)


''' execution
take string input from user
take another input as vowel and value is 'aeiouAEIOU'
creating c variable with 0 as value because we are assuming that given string might be empty 
taking string as deepak
iteration1: extract d from v and check the conditon if d in v or not,
            d not in v, c become 0
iteration2: extract e from s and check the conditon if e in v or not,
            e  in v, c become 1
iteration3: extract e from s and check the conditon if e in v or not,
            e in v, c become 2
iteration4: extract p from s and check the conditon if p in v or not,
             p not in v, c same 2
iteration5: extract a from s and check the conditon if a in v or not,
            a in v, c is become 3
iteration6: extract k from s and check the conditon if k in v or not,
            k not in v, c is same 3


            at last print c value is 3
'''