#wap to print absolute difference between sum of even digits and odd digits present in a given strings.
s=(input('value'))
even=0
odd =0
for i in s:
    if i.isdigit():
        i=int(i)
        if i%2==0:
            sum+=i
        else:
            i%2!=0
            odd+=i
print(sum)
print(odd)
''' execution
taking input as s
taking sum of even number as even and value as 0 i am assuming that given string might be empty
taking sum of odd number as odd and value as 0 i am assuming that given string might be empty
taking substring as 12356
iteration 1>> extract 1 from s and it is digit and it is not divisble by 2 so 
                this is odd number so odd=1
iteration 2>> extract 2 form s and it is digit and it is divisble by 2 so this is 
                     even number so even=2
iteration 3>> extract 3 from s and it is digit and it is not divisble by 2 so 
                  this is odd numbeer so odd=4
iteration 4>>  extract 4 from s and it is digit and it is divisble by 2 so thi is 
                      even number so even  =6
iteration 5>>   extract 5 from s and it is digit and it is not divisble by 2 so this is 
                        odd number so odd=9
iteration 6>>   extract 6 from s and it is digit and it is not divisble by 2 so this is 
                        even number so even=12
at last print even=12     sum of even
at last print odd=9         sum of even'''
