L=[14,25,98,75,23,1,4,56,59]
n=int(input("请输入一个数字:"))
m=len(L)
s=0
for i in L[:n]:
    s=s+i**2
    print(s)
