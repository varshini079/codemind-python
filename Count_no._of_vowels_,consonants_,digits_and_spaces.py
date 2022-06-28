s=input()
v=0
c=0
d=0
z=0
for i in s:
    if i in "aeiou":
        v=v+1
    elif i in "0123456789":
        d=d+1
    elif i==' ':
        z=z+1
    else:
        c=c+1
print("Vowels:" ,v)
print("Consonants:",c)
print("Digits:" ,d)
print("White spaces:",z)