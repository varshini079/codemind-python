def gcd(a,b):
    if(a>b):
        a,b=b,a
    for i in range(1,b+1,1):
        if a%i==0 and b%i==0:
            c=i
    return(c)
x,y=map(int,input().split())
print(gcd(x,y))