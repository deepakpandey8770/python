#wap to print every second even number in given range.
ll=int(input('value'))
ul=int(input('value'))
l=[]
for n in range(ll,ul+1):
    if n%2==0:
       l.append(n)
print(l[1::2])

'''execution 
taking lower limit ll as input from user
taking upper limt ul as input from user
taking list= empyt list because i am assuming that given range is empty
taking lower limit as 1
taking upper limit as 10

iteratios>>>
iteration1>>>execute 1 from given  range and check the conditon it even number or not 
              so it is not a even number so l remain []
iteration2>>> exectue 2 from given range and check the condition it even number or not
             so it is even number so l=[2]
iteration3>> execute 3 from given range and check the conditon it is even number or not 
            so it is not a even number so l ramian same  l[2]
iteration4>> execute 4 from given range and check the conditon it is even number or not 
            so it is even number so l =[2,4]
iteration 5>>> execute 5 from given range and check the condition it is even number or not
            so it is not a even number so ramain same l=[2,4]
iteration 6>>  execute 6 from given range and check the conditon it is even number or not
           so it is even number so l=[2,4,6]
iteration 7>>> execute 7 from given range and check the condition it is even number or  not 
           so it is not a even number so ramain same l=[2,4,6]
iteration 8>> execute 8 from given range and check the condition it is  even number or not
            so it it even number so l=[2,4,6,8]
iteration9>>> execute 9 from given range and check the conditon it is even number or not  
            so it is not a even  number so l ramain same[2,4,6,8]
iteration10>> execute 10 from given  range and check the conditon it is even number or not 
            so it is even number so l=[2,4,6,8,10]

at last print the value of l in second updation value
so        l=[2,6,10]



'''