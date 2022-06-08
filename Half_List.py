n=int(input())
l=list(map(int,input().split()))
t=n//2
c=1
for i in range(t,n,1):
    print(l[n-c],end=' ')
    c=c+1
for i in range(0,t):
    print(l[i],end=' ')
