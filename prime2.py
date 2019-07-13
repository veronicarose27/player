ab=int(input())
l=[]
for i in range (2,ab+1):
    if(ab%i)==0:
        l.append(i)
        ab=ab//i
s=sorted(l)
print(*s)
