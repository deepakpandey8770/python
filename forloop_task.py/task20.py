#wap to print every third even number in given range.
ll=int(input('value:'))
ul=int(input('value:'))
l=[]
for n in range(ll,ul+1):
    if n%2==0:
        l.append(n)
print(l[2::3])

'''executions
taking ll as input from user 
taking ul as input from user 
taking l=[] for storing in it
taking lower limit as 1
taking upper limit as 12
iterations//////
iteration1>> execute 1 from given range and check the condtion it is even or not 
            so it is not even number so l=[]
iteration2>> execute 2 from given range and check the condition it is even or not
             so it is even number so l=[2]
iteration3>> execute 3 from given range and check the condition it is even or not 
            so it is not even number so l ramin same l=[2]
iteration4>> execute 4 from given range and check the conditon it is even or not
            so it is even number so l =[2,4]
itetaiton5>> execute 5 from given range and check the conditon it is even or not
            so it is not a even number so l=[2,4]
iteration6>> execute 6 from given range and check the condition it is even or not
            so it is even number so l=[2,4,6]
iteration7>> execute 7 from given range and check the condition it is even or not
            so it is not even number so l=[2,4,6]
itetation8>> execute 8 from given range and check the condition it is even or not 
            so it is even number so l=[2,4,6,8]
iteration9>> execute 9 from given range and check the condition it is even or not
            so it is not a even number so l=[2,4,6,8]
iteration10>> execute 10 from given range and check the conditon it is even or not 
            so it is even number so l=[2,4,6,8,10]
iteration11>> execute 11 from given range and check the codition it is even or not
            so it is not a even number so l=[2,4,6,8,10]
iteration12>> execute 12 from given range and check the condition it is even or not
            so it is even number so l=[2,4,6,8,10,12]

at last print the value of l in updation of 3 and sip is 2
so l=[6,12]




'''