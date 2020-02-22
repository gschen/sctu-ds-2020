#1、求给定数的阶乘
a=int(input('请输入整数:'))
b=1
if a == 0:
    print('0的阶乘为1')
elif a < 0:
    print('负数没有阶乘')
else:
    for i in range(1,a+1):
        b=b*i
print('%d的阶乘是%d'%(a,b))



#单利公式为：单利=（P x T x R）/ 100其中，P是本金,T是时间，R是利率
P=int(input('P='))
R=int(input('R='))
T=int(input('T='))
y=(P*R*T)/100
print(y)



#查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]
list1=[14,25,98,75,23,1,4,56,59]
print("最大元素:",max(list1))


#4、求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定
list1=[14,25,98,75,23,1,4,56,59]
n=int(input("请输入整数："))
l=list1[:n]
def Pingfang(*l):
    i=0
    for m in l:
        i+= m**2
    return i
print(Pingfang(*l))


#5.交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
list1=[14,25,98,75,23,1,4,56,59]
a=int(input("请输入要替换的位置："))
b=int(input("请输入要替换的位置："))
list1[a],list1[b]=list1[b],list1[a]
print(list1)




