n,m=map(int,input().split())
l=(list(map(int,input().split())))
l1=list(map(int,input().split()))
p=[]
for i in l:
    if i not in p:
        p.append(i)
for i in p:
    if i in l and i in l1:
        print(i,end=' ')


    