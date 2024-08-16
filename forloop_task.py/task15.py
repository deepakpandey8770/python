#wap to find the factorial of a given number.
n=int(input('value'))
fact=1   #c=1 becz 0 factorial is 1 that's why we take 0
for i in range(1,n+1):
    fact*=i
print(fact)

'''execution 
taking input from user
taking fact as 1  ==because fatorial of 0 is 1
taking input as5
iteration:
iteration1: extract 1 from n and checking the condition fact*1  so fact
            fact=1

iteraiton2: extract 2 from n and checking the condition fact*2 so 
            fact=2
iteration3: extract 3 from n and checking the condeition fact*3 so
            fact become 6
iteration 4: extract 4 from n and checking the condition fact*4 so
             fact become 24
iteration 5: extract 5 from n and checking the condition fact *5 so 
             fact become 120 

at last print the value of fact is 120

'''