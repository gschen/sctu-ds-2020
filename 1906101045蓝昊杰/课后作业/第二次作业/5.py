x,y,z=map(int,input().split())
l=[x,y,z]
m=n=len(l)-1
for j in range(m):
    for i in range(n):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    n-=1
print(l)