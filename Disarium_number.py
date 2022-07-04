def dis(n):
    s=0
    while(n>0):
        t=n%10
        s=s+t**(len(str(n)))
        n=n//10
    return(s)
n=int(input())
if (dis(n)==n):
    print(True)
else:
    print(False)