#wap to find absolute difference between of sum of even number  and sum of odd number in given list.
s=[11,2,100,20,1]
es=0
os=0
for i in s:
    if i%2==0:
        es+=i
    else:
        os+=i
print(abs(es-os))

'''execution 
taking list as[11,2,100,20,1]
taking es=0 i am assuming that given list is 0 even number
taking os =0 i am assuming that given list is 0 odd number 
iterates over each element i in the list s.
itearation1: extract 11 from s and check the conditon it is i%2==0 or not so
              es value 0  and os value=11
iteration 2: extract 2 from s and check the conditon it is i%2==0 or not so
              es value become 2 and os value ramain same 11
iteration 3: extract 100 from s and check the conditon it is i%2==0 or not so
             es value become 102 and os value reamin same 11
iteration 4: extract 20 from s and check the conditon it is i%2==0 or not so
             es value become 122 and os value remain same 11
iteration 5: extract 1 from s and check the conditon it is i%2==0 or not so
             es value remain same 122 and os value become 12

at last print the the absolute value of es is 122 and os is 12
so es-os so the absolute difference is 110'''