def fib(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a,b=b,c
        if(c==n):
            return(True)
    else:
        return(False)
n=int(input())
i=1
while(True):
    if fib(n-i) and fib(n+i):
        print(n-i,n+i)
        break
    elif fib(n-i):
        print(n-i)
        break
    elif fib(n+i):
        print(n+i)
        break
    i=i+1