#wap to print altenate even number in given range.
ll=int(input('value:'))
ul=int(input('value:'))
l=[]
for n in range(ll,ul+1):
    if n%2==0:
        l.append(n)
print(l[::2])


'''executions
taking ll limit from user
taking ul limit from user
taking l=[] we are assuming that given range is empty.
taking ll as 1
takinng ul as 10

iterations>>
iteration1: execute 1 from range and checking the condition it is even number or not
            so it is not a even number so l []
iteration2: execute 2 from range and checking the condition it is even number or not 
            so it is a even number so l [2]
iteration3: execute 3 from range and checking the condition it is even number or not 
           so it is not a even number so l remain same l=[2]
iteration4: execute 4 from range and checking the condition it is even number or not 
           so it is even number so l=[2,4]
iteration5: execute 5 from range and  checking the condition it is even number or not
        so it is not a even number so l ramain same l=[2,4]
iteration6: execute 6 from range and checking the conditon it is even number or not 
            so it even number so l become [2,4,6]
iteration7: extract 7 from range and checking the condition it is even number or not
           so it not a even number so l remain same
iteration 8: extract 8 from range and checking the condition it is even number or  not 
           so it is even number so l become [2,4,6,8]
iteraiton 9: extract 9 from range and checking the conditon it is even number or not
           so it is not a even number so l ramain same
iteration10: extract 10 from range and checking the conditon it is even number or not 
           so it is even number so l become[2,4,6,8,10]

at last print the value of l in updation value of 2
then the alternate even number is [2,6,10]`

'''