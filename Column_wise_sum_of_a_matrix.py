n,k=map(int,input().split())
l=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
l1=[]
for i in range(k):
    p=[]
    for j in range(n):
        p.append(l[j][i])
    l1.append(p)
for i in l1:
    print(sum(i),end=" ")