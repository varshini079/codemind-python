n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    if (i%2==0):
        c=c+l[i]
print(c)