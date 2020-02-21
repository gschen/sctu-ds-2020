L=[14,25,98,75,23,1,4,56,59]
n=int(input())
m=list(L[:n])
s=0
for i in m:
    s=s+i**2
print(s)