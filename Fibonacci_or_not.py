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
print(fib(n))
    