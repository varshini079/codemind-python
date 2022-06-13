s=int(input())
def pal(s):
    r=str(s)
    t=int(r[::-1])
    if (s==t):
        return(True)
    else:
        return(False)
for i in range(1,s):
    if pal(s-i)and pal(s+i):
        print(s-i,s+i)
        break
    elif pal(s-i):
        print(s-i)
        break
    elif pal(s+i):
        print(s+i)
        break
