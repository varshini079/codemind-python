def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return(False)
                break
        else:
            return(True)
n=int(input())
for i in range(2,n):
    if(n%i==0 and prime(i)):
        t=n//i
        print(i,t)
        break
else:
    print("-1")