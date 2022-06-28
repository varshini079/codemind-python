s=input()
p=s.lower()
t=len(s)
c=0
for i in range (t):
    c=c+1
    if p.count(p[i])==1:
        print(i)
        break
if(t==c):
    print(-1)