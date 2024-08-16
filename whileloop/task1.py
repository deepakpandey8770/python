#wap to print the sum of first n numbers by using while loop
n=int(input('value:'))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)


'''executions 
taking integer input from user 
taking sum=0 bcz i am assuming that total sum is 0
taking i=1 we are initiatlizing a variable as a first step for while
taking input as 4

iterations....
iteration1>> execute 1 from given n and check the condition i<=n or not so it is less than i so conditon is true
             so add in sum and sum become 1
iteration2>> execute 2 from given n and check the condition  i<=n or not so it is less than i so condition is true 
            so add in sum and sum become 3
iteration3>> execute 3 from given n and check the condition i<=n or not so it is less than i so condition is true
            so add in sum and sum becom 6
iteration4>> execute 4 from given n and check the condition i<=n or not so it is less than i so condition is true
            so add in sum and sum become 10
        
at last print the value of sum =10


'''