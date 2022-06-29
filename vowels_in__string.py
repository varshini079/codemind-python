s=input()
k=[]
l=[]
for i in s:
    if i in "aeiouAEIOU":
        k.append(i)
for i in k:
    if i not in l:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(*l)