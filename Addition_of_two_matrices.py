n=int(input())
l1,l2=[],[]
for i in range(n):
    m=list(map(int,input().split()))
    l1.append(m)
for i in range(n):
    m=list(map(int,input().split()))
    l2.append(m)
l3=[]
for i in range(n):
    p=[]
    for j in range(n):
        p.append(l1[i][j]+l2[i][j])
    l3.append(p)
for i in range(n):
    print(*l3[i])