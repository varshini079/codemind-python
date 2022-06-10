def hn(n):
    s=0
    while(n>0):
        r=n%10
        s=s+(r)**2
        n=n//10
    return(s)
n=int(input())
t=len(str(n))
while(t>=2):
    n2=hn(n)
    n=n2
    t=len(str(n))
if(n2==1 or n2==7):
    print(True)
else:
    print(False)
    
    
    