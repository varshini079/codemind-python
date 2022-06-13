def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return(False)
        else:
            return(True)
t=int(input())
for i in range(t):
    j=int(input())
    for i in range(j):
        if prime(j-i):
            print(j-i)
            break
        elif prime(j+i):
            print(j+i)
            break
        
    