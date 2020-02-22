
#1.求给定数的阶乘
a=int(input('please enter:'))
b=1
if a == 0:
    print('0的阶乘为1')
if a < 0:
    print('负数没有阶乘')
else:
    for i in range(1,a+1):
        b=b*i
print('%d的阶乘是%d'%(a,b))


#2.单利公式
P=int(input('P='))
R=int(input('R='))
T=int(input('T='))
y=(P*R*T)/100
print('输出:%d'%(s))


#3.找数组中最大元素
listl=[14,25,98,75,23,1,4,56,59]
maxl=max(listl)
print('最大值是:%d'%maxl)


#4.求前n个属平方和
listl=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入整数：'))
l=listl[:n]
def Tang(*l):
    i=0
    for m in l:
        i=i+(m**2)
    return i
print(Tang(*l))




#5.交换列表元素
listl=[14,25,98,75,23,1,4,56,59]      #默认第一个元素的位置是0
a=int(input('请输入要替换的位置：'))
b=int(input('请输入要替换的位置：'))
listl[a],listl[b]=listl[b],listl[a]
print(listl)


