def pal(n):
    t=str(n)
    r=int(t[::-1])
    if(r==n):
        return(True)
    else:
        return(False)
n=int(input())
for i in range(n):
    x=int(input())
    print(pal(x))