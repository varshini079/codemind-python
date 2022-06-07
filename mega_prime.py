def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return(False)
                break
        else:
            return(True)
n=int(input())
t=str(n)
if(prime(n)==False):
    print("Not Mega Prime")
if(prime(n)):
    for i in range(len(t)):
        t=n%10
        if(prime(t)):
            n=n//10
            if(prime(n)):
                print("Mega Prime")
                break
    else:
        print("Not Mega Prime")