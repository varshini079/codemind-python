def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                break
        else:
            return(True)
c=0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(prime(i)):
        c=c+1
print(c)