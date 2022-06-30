s=input()
c=0
l=[]
for i in range(len(s)):
    if s[i]==' ' or i==(len(s)-1):
        if i==(len(s)-1):
            l.append(c+1)
            break
        l.append(c)
        c=0
    else:
        c=c+1
if(len(s)==0):
    print(c)
else:
    print(min(l))