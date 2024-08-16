#wap to check how many vowels and how many consonent are there in given sting

s=input()
v='aeiouAEIOU'
vc=0
cc=0

for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(vc)
print(cc)


''' execution
take string input from user
take another input as vowel and value is 'aeiouAEIOU'
creating vc variable with 0 as value because we are assuming that given string might be empty 
creating cc variable with 0 as value because we are assuming that given string might be empty
taking string as anuj
iteration1: extract a from s and check the conditon if a in v or not,
            a in v, so vc become 1 and cc become 0
iteration2: extract n from s and check the conditon if n in v or not,
            n not in v, so vc same 1 and cc become 1
iteration3: extract u from s and check the conditon if u in v or not,
            u in v, so vc become 2 and cc same 1
iteration4: extract j from s and check the conditon if j in v or not,
             j not in v, vc same 2 and cc become 2

at last print vc value is 2
at last print cc value is 2
'''