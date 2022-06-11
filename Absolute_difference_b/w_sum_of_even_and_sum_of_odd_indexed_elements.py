n=int(input())
l=list(map(int,input().split()))
c=t=0
for i in range(0,n):
    if (i%2!=0):
        c=c+l[i]
    elif(i%2==0):
        t=t+l[i]
print(abs(c-t))