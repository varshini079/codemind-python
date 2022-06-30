s=input()
res = [i for j in s.split() for i in (j, ' ')][:-1]
c=0
for i in res:
    if i==" ":
        c=c+1
print(c+1)