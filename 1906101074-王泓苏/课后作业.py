# 第一题
def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*func(n-1))
a=func(5)
print(a)

#第二题
P=int(input())
T=int(input())
R=int(input())
m=(P*T*R)/100
print(m)

#第三题
L=[14,25,98,75,23,1,4,56,59]
L.sort()
print(L[-1])

#第四题
L=[14,25,98,75,23,1,4,56,59]
n=int(input())
s=0
if n<len(L):
    while n>0:
        s=s+L[n-1]**2
        n=n-1
print(s)

#第五题
lis=[14,25,98,75,23,1,4,56,59]
x,y=map(int,input("请输入两个数").split())
lis[x],lis[y] = lis[y],lis[x]
print(lis)

