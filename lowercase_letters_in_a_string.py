s=input()
c=0
for i in s:
    if ord(i) in range(97,122):
        c=c+1
print(c)