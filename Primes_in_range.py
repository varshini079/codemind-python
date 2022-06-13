n=int(input())
m=int(input())
s=0
def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return(False)
        else:
            return(True)
for i in range(n,m+1):
    if(prime(i)):
        s=s+1
print(s)
