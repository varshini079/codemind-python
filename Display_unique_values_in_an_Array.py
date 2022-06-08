n=int(input())
l=list(map(int,input().split()))
q=list(set(l))
p=[]
for i in q:
    if l.count(i)==1:
        p.append(i)
if(len(p)==0):
    print(-1)
else:
    print(*p)
