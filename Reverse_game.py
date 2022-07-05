n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    t=str(i)
    t=int(t[::-1])
    p.append(t)
print(*p)