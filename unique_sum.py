n=int(input())
l=list(set(list(map(int,input().split()))))
c=0
for i in l:
        c=c+i
print(c)