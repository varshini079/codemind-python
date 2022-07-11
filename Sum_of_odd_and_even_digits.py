n=int(input())
l=list(map(int,input().split()))
s,t=0,0
for i in range(n):
    if i%2==0:
        s=s+l[i]
    else:
        t=t+l[i]
if (s-t==0):
    print("YES")
else:
    print("NO")