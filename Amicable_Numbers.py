n=int(input())
p=int(input())
s=0
q=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        s=s+i
for i in range(1,(p//2)+1):
    if(p%i==0):
        q=q+i
if(s==p and q==n):
    print("Amicable")
else:
    print("Not Amicable")