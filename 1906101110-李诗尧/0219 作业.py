# 1、求给定数的阶层
n=int(input('输入一个数:'))
m=1
if n>0 and n!=1 and n!=10 and n!=20 and n!=30 and n!=40 and n!=50:
    for i in range(1,n+1):
        m=m*i
    print('阶层为：',m)
elif n<0:
    print('负数无阶层')
else:
    print('阶层为1')

# 2、求单利
P=int(input('输入一个数：P='))
T=int(input('输入一个数：T='))
R=int(input('输入一个数：R='))
m=(P*T*R)/100
print("单利为：%d"%(m))

# 3、查找数组中最大元素
lis1=[14,25,98,75,23,1,4,56,59]
max=max(lis1)
print(max)

# 4、求数组中前n个数的平方和：[14,25,98,75,23,1,4,56,59]
lis1=[14,25,98,75,23,1,4,56,59]
m=len(lis1)
s=0
n=int(input())
if n<=m and n>0:
    for i in range(0,n):
        s=lis1[i]*lis1[i]+s
    print('平方和：',s)
else:
    print('无平方和')
    


# 5、交换列表中任意两个元素 [14,25,98,75,23,1,4,56,59]
n,m=map(int,input().split( ))
lis1=[14,25,98,75,23,1,4,56,59]
a=lis1[n-1]
b=lis1[m-1]
lis1[n-1]=b
lis1[m-1]=a
print(lis1)

