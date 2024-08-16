#wap to print sum of even digit present in a given string
s=input('value')
sum=0
for i in s:
    if i.isdigit():
        i=int(i)
        if i%2==0:
            sum+=i
print (sum)

''' execution.
takeing  string inputs from user
creating si variable with s,0 as value because we are assuming that given string might be empty
taking stirng as 123456
Iteration 1: Extracting 1 from the s it is a digit but not even so it is skipped
                the sum remains 0
Iteration 2: Extracting 2  from the s it is an even digit  so it is added to the sum
                sum becomes 2
Iteration 3: Extracting 3from the s  iti s a digit but not even so it is skipped
                the sum remains 2
Iteration 4: Extracting 4 from the s it is an even digit so it is added to the sum 
                 sum becomes 6
Iterations 5  Extracting 5 from the s  it is a digit but not even so it is skipped 
                 the sum remains 6
Iteration 6: Extracting 6 from the s it is an even digit so it is added to the sum 
                 sum becomes 12
at last print the value of sum is 6'''