#function without arguments and without return type 
"""def selling_vegetables():
    print('tomato')
    print('apples')
    print('orange')
for i in range(1,30):
    selling_vegetables()"""

#function with arguments and without return type 
"""def selling_vegetable(a,b):
    print(a)
    print(b)
    print(a+b)
selling_vegetable(1,3)"""

#function with arguments and without return type 
n=int(input('value'))
star=1

for row in range(1,n+1):
    dummy=1
    for col in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
        
    print()
    star-=1
    
    


