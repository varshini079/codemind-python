n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if(i**0.5-int(i**0.5)==0):
        s=s+(i)
print(s)
    