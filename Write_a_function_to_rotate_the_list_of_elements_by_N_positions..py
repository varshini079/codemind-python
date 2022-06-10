n=int(input())
l=list(map(int,input().split()))
r=int(input())
for i in range(r):
    l.insert(0,l.pop())
print(*l)