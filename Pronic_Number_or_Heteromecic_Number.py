n=int(input())
if(n==0):
    print("YES")
for i in range(1,(n//2)+1):
    if(n==i*(i+1)):
        print("YES")
        break
else:
    print("NO")
        