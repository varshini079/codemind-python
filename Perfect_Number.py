n=int(input())
i=1
s=0
while i<(n//2)+1:
    if(n%i==0):
      s=s+i
    i=i+1
if(s==n):
    print("True")
else:
    print("False")
        
    