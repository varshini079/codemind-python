t=int(input())
l=list(map(int,input().split()))
k=list(set(l))
n=[]
for i in k:
    z=l.count(i)
    n.append(z)
b=max(n)
k.sort() 
for i in k:
    if l.count(i)==b:
        print(i)
        break