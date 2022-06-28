n=int(input())
for i in range(n):
    s=input()
    for t in s: 
        if t.isdigit():
            print("Yes")
            break
    else:
        print("No")