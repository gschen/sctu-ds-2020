#1、	求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
x=1
a=int(input("给定一个数："))
if a==1 or a==10 or a==20 or a==30 or a==40 or a==50 :
    raise ValueError
else:
    for i in range(1,a+1):
        x=x*i
    print(x)

#2、	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
#例如输入：P = 10000 
# R = 5 
# T = 5  
# 输出：2500
#要求:P、T、R都是input输入的，不能固定。
P=int(input('P='))
T=int(input('T='))
R=int(input('R='))
S=(P*T*R)/100
print('%d'%S)

#3、	查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]。
list1=[14,25,98,75,23,1,4,56,59]
print(max(list1))

#4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。
s=0
n=int(input())
list2=[14,25,98,75,23,1,4,56,59]
if n > len(list2) :
    print('n大于数组长度')
else:
    for i in list2[:n]:
        s=s+i**2
    print(s)

#5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入。 
lis=[14,25,98,75,23,1,4,56,59]
m,n=map(int,input('输入两个置换元素的位置：').split(','))
a=lis[m]
lis[m]=lis[n]
lis[n]=a
print(lis)