n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
c=[]
for i in l:
     c.append(len(str(i)))
t=max(c)
l=l[::-1]
for i in l:
    if len(str(i))==t:
        print(i,end=' ')
         
