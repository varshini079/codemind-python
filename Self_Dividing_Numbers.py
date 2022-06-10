def sd(n):
    l=map(int,str(n))
    c=0
    p=len(str(n))
    for i in l:
        if(i==0):
            return(False)
        elif(n%i==0):
            c=c+1
    if(c==p):
        return(True)
x=int(input())
y=int(input())
for i in range(x,y+1):
    if(sd(i)):
        print(i,end=" ")