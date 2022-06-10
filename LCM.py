def lcm(a,b):
    if(a>b):
        i=a
        t=a
    else:
        i=b
        t=b
    while(True):
        if i%a==0 and i%b==0:
            return(i)
        i=i+t
a,b=map(int,input().split())
t=(lcm(a,b))
print(t)
    