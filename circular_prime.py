n=int(input())
t=str(n)[::-1]
t=int(t)
c=0
h=0
i=2
p=2
while(i<(n//2)+1):
    if(n%i==0):
        c=c+1
    i=i+1    
while(p<(t//2)+1):
    if(t%p==0):
        h=h+1
    p=p+1    
if(c==0 and h==0):
    print("circular prime")
elif(c==0 or h==0):
    print("prime but not a circular prime")
else:
    print("not prime")
    
    
    
    
    
    
        