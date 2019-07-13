u=input()
p=list(u)
k=[]
for i in p:
    a=ord(i)+3
    y=chr(a)
    k.append(y)
print("".join(k))
