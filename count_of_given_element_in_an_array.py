n=int(input())
l=list(map(int,input().split()))
t=int(input())
if t in l:
    print(l.count(t))
else:
    print(0)