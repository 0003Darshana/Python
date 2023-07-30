n=int(input())
m=int(input())
a=[]
sum=0
for i in range(n,m+1):
    a.append(i)
    b=len(a)
    sum+=i
    avg=sum/b
print(avg)

