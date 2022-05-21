l,b,c=map(int,input().split())
s=(l+b+c)/2
t=((s)*(s-l)*(s-b)*(s-c))**0.5
print("%0.2f"%t)