n=int(input())
a=[]
for i in range(0,n):
    e=int(input())
    a.append(e)
for i in a:
    if(i**0.5-int(i**0.5)==0):
        print("True")
    else:
        print("False")