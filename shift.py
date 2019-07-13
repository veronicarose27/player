a,b=map(int,input().split())
p=list(map(int,input().split()))
for i in range(0,b):
    p=[p[-1]]+p[:-1]
print(*p)
