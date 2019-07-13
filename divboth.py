c,d=map(int,input().split())
o=max(c,d)
for i in range(o,10000000):
    if((i%c==0) and (i%d==0)):
       print(i)
       break

