#wap to print the even number in given range

ll=int(input('value'))
ul=int(input('value'))
for n in range(ll,ul+1):
    if n%2==0:
        print(n)

'''execution 
taking lower limit  input from user
taking upper limit input from user
taking lower limit 1
taking lower limit 10
iterations:
iteration1: extract 2 from range and checking the condition and 
            print 2 is even number
iteration2: extract 3 from range and checking the condition and 
            even number ramian same =3
iteration3: extract 4 from range and checking the conditon and 
            print 4 is even number 
iteration 4: extract 5 from range and checking the conditon and 
            5 is not even number so even number remain same 4
iteration 6: extract 6 from range and checking the conditon and 
            6 is even number so print even number as 6
iteration 7: extract 7 from range an d checking the conditon and 
             7 is not even nubmer so even number ramain same
iteration 8: extract 8 from range and checking the condition and 
            8 is even number so print even number =8
itertaion 9: extract 9 from range and checking the condition and
            9 is not a even number so even number ramain same
iteration 10: extract 10 from range and checking the conditon and 
            10 is even number so print even number=10

at last print the even number =2,4,6,8,10



'''