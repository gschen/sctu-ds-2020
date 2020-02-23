#第一题
x=1
n=int(input('输入一个整数：'))
for i in range(1,n+1):
    x=x*i
print(n,'!=',x)
#第二题
P=int(input('P='))
R=int(input('R='))
T=int(input('T='))
a=(P*R*T)/100
print(a)
#第三题
a=[14,25,98,75,23,1,4,56,59]
max=max(a)
print(max)
#第四题
list1=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入一个整数：'))
i=0
if n<len(list1):
    while n>0:
        i=i+list1[n-1]**2
        n-=1
print(i)
#第五题
list1=[14,25,98,75,23,1,4,56,59]
a=int(input('请输入替换的位置：'))
b=int(input('请输入替换的位置：'))
list1[a],list1[b]=list1[b],list1[a]
print(list1)