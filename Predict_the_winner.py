n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(n):
    if i%2==0:
        x.append(l[i])
    else:
        y.append(l[i])
if abs((sum(x)-sum(y)))%4==0:
    print("X")
else:
    print("Y")
    
    

    