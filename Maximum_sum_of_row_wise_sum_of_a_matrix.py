n,k=map(int,input().split())
a=[]
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in l:
    a.append(sum(i))
print(max(a))