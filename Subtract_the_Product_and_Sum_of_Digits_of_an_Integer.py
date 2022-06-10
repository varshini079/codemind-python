n=int(input())
t=len(str(n))
s=0
p=1
for i in range(t):
    r=n%10
    s=s+r
    p=p*r
    n=n//10
print(p-s)