n,k=map(str,input().split())
N=len(n)
M=len(k)
if(N!=M):
    print("no")
else:
    for i in n:
        o=n.count(i)
    for j in k:
        p=k.count(j)
if(o==p):
    print("yes")
else:
    print("no")
        
