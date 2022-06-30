n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    i=abs(i)
    c.append(len(str(i)))
print(*c)
