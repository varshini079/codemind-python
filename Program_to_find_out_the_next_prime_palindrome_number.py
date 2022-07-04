def pal(n):
    t=str(n)
    p=int(t[::-1])
    if p==n:
        return(True)
    return(False)
def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return(False)
                break
        return(True)
n=int(input())
n=n+1
while(n):
    if prime(n) and pal(n):
        print(n)
        break
    n=n+1