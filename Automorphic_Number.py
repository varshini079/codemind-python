n=int(input())
q=len(str(n))
t=n*n
r=t%(10**q)
if(n==r):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")