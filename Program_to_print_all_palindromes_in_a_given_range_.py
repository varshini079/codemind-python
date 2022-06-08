n=int(input())
m=int(input())
def pal(q):
    t=str(q)
    r=int(t[::-1])
    if(r==q):
        return True
for w in range(n,m+1):
    if(pal(w)):
        print(w,end=" ")
        
            