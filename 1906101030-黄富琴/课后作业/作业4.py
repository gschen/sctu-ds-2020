L=[14,25,98,75,23,1,4,56,59]
n=int(input("请输入一个数字:"))
m=len(L)
S=0
for i in L[:n]:
    S=S+i**2
    print(S)
