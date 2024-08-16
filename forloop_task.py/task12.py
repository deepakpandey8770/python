#wap to find maximum number in given list, use built in method.
L=[11,22,100,20,1]
mx=0
for i in L:
    if i>mx:
        mx=i
print (mx)

'''execution  
taking list of number as input
taking mx=0 bcz i assuming given list is 0
iteration1: extract 11 from l and check i>mx  max or not so i is max
            so mx value is 11
iteration2: extract 22 from l and check i>mx  max or not it is greter than mx
            so mx value is 22
iteration3: extract 100 from l and check i>mx max or not it is greter than mx 
            so mx value become 100
iteration4: extract 20 from l and check i>mx max or not it is not gretar than mx
            so mx value remain same 100
iteration5: extract 1 from l and check i>mx max or not it is not gretar than mx
            so mx value remain same 100
            
at last print the value of mx is 100'''