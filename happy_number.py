def hn(num):
    r=s=0
    while num>0:
        r=num%10
        s=s+(r*r)
        num=num//10
    return s
num=int(input())
n1=num
while(n1!=1 and n1!=4):
    n1=hn(n1)
if n1==1 or n1==7:
    print(True)
else:
    print(False)