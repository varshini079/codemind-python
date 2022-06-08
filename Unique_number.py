n=int(input())
t=len(str(n))
l=list(map(int,str(n)))
r=len(list(set(l)))
if r==t:
    print("Unique Number")
else:
    print("Not Unique Number")
    