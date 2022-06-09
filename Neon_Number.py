n=int(input())
t=(n*n)
s=0
while(t>0):
    q=t%10
    s=s+q
    t=t//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")