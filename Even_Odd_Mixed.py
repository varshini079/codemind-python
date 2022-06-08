n=int(input())
l=list(map(int,str(n)))
c=0
t=0
for i in range(len(l)):
    if l[i]%2==0:
        c=c+1
    if l[i]%2!=0:
        t=t+1
if(c+t==len(l) and c!=0 and t!=0):
    print("Mixed")
elif(c==0 and t>0):
    print("Odd")
elif(c>0 and t==0):
    print("Even")
    
        