def fac(n):
    t=1
    for i in range(1,n+1):
        t=t*i
    return (t)
n=int(input())
for i in range(n):
    t=int(input())
    q=fac(t)
    print(q)