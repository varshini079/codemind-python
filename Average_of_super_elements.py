n=int(input())
l=list(map(int,input().split()))
p=list(set(l))
s=0
c=0
for i in p:
    if l.count(i)==i:
        s+=i
        c=c+1
if s==0:
    print(-1)
else:
    print("%.2f"%(s/c))