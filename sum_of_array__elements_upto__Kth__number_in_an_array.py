n=int(input())
c=0
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    c=c+l[i]
print(c)