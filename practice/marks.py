def firstindex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerlist=a[1:]
    smallerlistoutput=firstindex(smallerlist,x)
    if smallerlistoutput==-1:
        return -1
    else:
        return smallerlistoutput+1
firstindex([1,2,3,4,5],6)    
