#wap to print how many special character are present in given string
s=input('value')
sc=0
for i in s:
    if not  i.isalnum():
        sc+=1
print (sc)

'''execution
taking input as s
taking special character as sc and value as 0 bcz i am assuming that given string might empty
taking input as !1@2#3
iteration1>>extrat ! from s and ! is a special character so 
                  sc=1
iteration 2>>extract 1 from sand 1 is not a special character so skip
                    and sc ramain same 1
iteration 3>> extract @ from s and @ is a special character so 
                  sc=2
iteration 4>> extract 2 from s and 2 is not a special character so
                     skip and sc ramain same 2
iteration 5>> extract # from s and # is a special character so 
                        sc=3
iteration 6>> extract 3 from s and 3 is not a special character so
                     skip and sc remain same 3
at last print sc and value is 3''' 