n=int(input())
l=list(map(int,input().split()))
p=[]
t=[]
for i in l :
    if i not in p:
        p.append(i)
for i in p:
    if l.count(i)==i:
        t.append(i)
if len(t)==0:
    print(-1)
else:
    print(*t)