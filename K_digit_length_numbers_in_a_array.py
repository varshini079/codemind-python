n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    i=abs(i)
    if len(str(i))==k:
        c=c+1
print(c)