t=int(input())
n=t
s=0
def fac(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return(p)
while(t>0):
    q=t%10
    s=fac(q)+s
    t=t//10
if(s==n):
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")