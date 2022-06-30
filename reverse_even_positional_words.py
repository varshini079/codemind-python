s=input()
res = [i for j in s.split() for i in (j, ' ')][:-1]
j=[]
j1=[]
def rev(i):
    return i[::-1]
for i in res:
    if i==" ":
        res.remove(' ')
for i in res:
    if res.index(i)%2==0:
        j.append(rev(i))
    else:
        j.append(i)
print(*j)