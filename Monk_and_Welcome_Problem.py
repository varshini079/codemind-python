n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(0,n):
    t=a[i]+b[i]
    c.append(t)
print(*c)