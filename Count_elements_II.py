n,m=map(int,input().split())
l=(list(map(int,input().split())))
l1=list(map(int,input().split()))
p=[]
for i in l+l1:
    if i not in p:
        p.append(i)
c=[]
for i in p:
    if i in l and i in l1:
        c.append(i)
s=0
for i in p:
    if i not in c:
        s+=1
print(s)