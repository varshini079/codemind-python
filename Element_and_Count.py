n=int(input())
l=list(map(int,input().split()))
p=[]
q=[]
for i in l:
    if i not in p:
        p.append(i)
for i in p:
    q.append(i)
    q.append(l.count(i))
print(*q)