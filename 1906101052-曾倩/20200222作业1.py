#1
a=int(input('请输入:'))
b=1
if a == 0:
    print('0的阶乘为1')
if a < 0:
    print('负数没有阶乘')
else:
    for i in range(1,a+1):
        b=b*i
print('%d的阶乘=%d'%(a,b))

#2
P=int(input('P='))
R=int(input('R='))
T=int(input('T='))
y=(P*R*T)/100
print('单利=%d'%(y))

#3
list=[14,25,98,75,23,1,4,56,59]
maxl=max(list)
print('最大值=%d'%maxl)

#4
list=[14,25,98,75,23,1,4,56,59]
a=int(input('请输入一个整数：'))
b=list[:a]
def Tang(*b):
    i=0
    for m in b:
        i=i+(m**2)
    return i
print(Tang(*b))

#5
list=[14,25,98,75,23,1,4,56,59]
m=int(input('输入替换的位置：'))
n=int(input('输入替换的位置：'))
list[m],list[n]=list[n],list[m]
print(list)