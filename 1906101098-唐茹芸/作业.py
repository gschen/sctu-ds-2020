#1、	求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。


list=[1,10,20,30,40,50]
x = int(input())
a = 1
      if x not in list:
           for i in range(1, x+1):
           a = a*i
print(a)





#2、	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
#例如输入：P = 10000
      #R = 5
      #T = 5
#输出：2500
#要求:P、T、R都是input输入的，不能固定。



P=input("请输入本金：")
T=input("请输入时间：")
R=input("请输入利率：")
x=(P*T*R)/100
print(x)




#3、	查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]。



list=[14,25,98,75,23,1,4,56,59]
list.sort()
print(list[0])



#4.求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。



list=[14,25,98,75,23,1,4,56,59]
t=input("请输入一个数n:")
if t<9:
    s=0
    for t in list:
        s=s+i*i
        return s
print(s)




#5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入。




list=[14,25,98,75,23,1,4,56,59]
x=input("被置换的第一个位置：")
y=input("被置换的第二个位置：")
list[x],list[y]=list[y],list[x]
print(list)




