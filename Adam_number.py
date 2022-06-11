def am(n):
    t=str(n)
    r=int(t[::-1])
    p=str(r**2)
    q=int(p[::-1])
    if(q==n**2):
        return(True)
    else:
        return(False)
n=int(input())
print(am(n))