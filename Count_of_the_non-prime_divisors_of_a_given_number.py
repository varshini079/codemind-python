n=int(input())
s=0
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return(False)
    else:
        return(True)
for i in range(2,n+1):
    if(n%i==0 and prime(i)==False):
        s=s+1
print(s+1)
