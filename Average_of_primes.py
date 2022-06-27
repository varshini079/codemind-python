n=int(input())
l=list(map(int,input().split()))
c=0
t=0
def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                break
        else:
            return(True)
for i in l:
    if prime(i):
        t=t+1
        c=c+i
print("%.2f"%(c/t))
