def se(n):
    l=list(map(int,str(n)))
    c=0
    for i in l:
        if(i!=0 and n%i==0):
            c=c+1
    if(c==len(str(n))):
        return(True)
    else:
        return(False)
    

n=int(input())
m=int(input())
for i in range(n,m+1):
    if(se(i)==True):
        print(i,end=' ')
        
            