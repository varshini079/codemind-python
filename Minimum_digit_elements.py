n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(len(str(i)))
print(c.count(min(c)))