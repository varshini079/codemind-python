n=int(input())
l=list(map(int,input().split()))
def add(n):
    s=0
    while(n>0):
        t=n%10
        s=s+t
        n=n//10
    return(s)
r=0
for i in l:
    if i>9:
        r=r+add(i)
    else:
        r=r+i
print(r)
