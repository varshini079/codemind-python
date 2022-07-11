n=int(input())
w=[]
s=0
for i in range(n):
    w.append(int(input()))
t=int(input())
for i in w:
    if i<=t:
        s+=1
    else:
        s+=2
print(s)

