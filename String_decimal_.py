n=int(input())
for i in range(n):
    c=0
    s=input()
    for i in s:
        if i in "1234567890":
            c=c+1
    if(c==len(s)):
        print("True")
    else:
        print("False")