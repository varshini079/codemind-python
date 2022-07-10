n=int(input())
l=list(map(int,input().split()))
t=[]
p=[]
for i in l:
    i=abs(i)
    t.append(i)
for i in t:
    i=i*i
    p.append(i)
p.sort()
print(*p)