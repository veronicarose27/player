p=int(input())
sum=0
while(p>0):
    r=p%10
    s=r*r
    sum=sum+s
    p=p//10
print(sum)
