def pal(n):
    t=str(n)
    t=int(t[::-1])
    if n==t:
        return(True)
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i):
        c=c+1
print(c)
    