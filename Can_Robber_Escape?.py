n=int(input())
c=0
l=[]
l=list(map(int,input().split()))
for q in l:
    if(q%2!=0):
        c=c+1
if(c<3):
    print("YES")
else:
    print("NO")