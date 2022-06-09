t=int(input())
s=0
p=1
while(t>0):
    q=t%10
    s=s+q
    p=p*q
    t=t//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")