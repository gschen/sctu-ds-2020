#1、	求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
def num(n):
    if n == 0:
         return  1
    sum = n * num(n - 1)
    return sum
print(num(4))


#2、	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
#例如输入：P = 10000
     # R = 5
      #T = 5
#输出：2500
#要求:P、T、R都是input输入的，不能固定
P=int(input('P='))
T=int(input('T='))
R=int(input('R='))
s=(P*T*R)/100
print(s)




#3,	查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]。
L=[14,25,98,75,23,1,4,56,59]
print(max(L))


#4,求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59],要求：n需要是input输入，且小于数组长度，不能固定。
L=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入一个数:'))
s=0
if n<len(L) and n>0:
    for n in L:
        s+=n**2
        print(s)
else:
    print('错误')

#5、交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59],要求，被置换的两个位置需要input输入。
list=[14,25,98,75,23,1,4,56,59]
a,b = map(int,input().split())
list[a],list[b]=list[b],list[a]
print(list)