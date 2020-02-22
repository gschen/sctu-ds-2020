n=int(input("请输入n:"))
l=[14,25,98,75,23,1,4,56,59]
s=0
if n<len(l):
    while n>0:
        s=s+l[n-1]**2
        n=n-1
print(s)
