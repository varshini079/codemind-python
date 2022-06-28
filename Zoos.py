n=input()
x=0
for i in n:
    if i=='z':
        x=x+1
y=len(n)-x
if(2*x==y):
    print("Yes")
else:
    print("No")