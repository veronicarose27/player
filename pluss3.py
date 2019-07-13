p=input()
q=''
r='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in p:
    if i in r:
        t=r.index(i)
        t=t+3
        q=q+r[t]
print(q)
