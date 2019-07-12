nk=input()
n=list(nk)
N=len(n)
x=[]
for i in range(0,N,2):
  x.append(n[i+1])
  x.append(n[i])
res="".join(x)
print(res)
