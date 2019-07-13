p=int(input())
y=str(input())
y=list(y)
for i in y:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        y.remove(i)
o=y[::-1]
print("".join(o))
