# 1、	求给定数的阶乘
# 要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
num=int(input())
factorial=1
not_nums=[1,10,20,30,40,50]
if num not in not_nums:
    while num>1:
        factorial=factorial*num
        num-=1
    print(factorial)
else:
    print('你输出的数在要求之外')

# 2、	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
# 例如输入：P = 10000
#       R = 5
#       T = 5
# 输出：2500
P,R,T=map(int,input().split())
interest=(P*T*R)/100
print(interest)

# 3、	查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]。
li=[14,25,98,75,23,1,4,56,59]
max_num=max(li)
print(max_num)

# 4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
# 要求：n需要是input输入，且小于数组长度，不能固定。
li=[14,25,98,75,23,1,4,56,59]
n=int(input())
sum=0
if n<len(li):
    for x in li[:n]:
        sum=sum+x**2
    print(sum)
else:
    print('n超过了数组的长度')

# 5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
# 要求，被置换的两个位置需要input输入。
li=[14,25,98,75,23,1,4,56,59]
exchange_num1,exchange_num2=map(int,input().split(' '))
li[exchange_num1],li[exchange_num2]=li[exchange_num2],li[exchange_num1]
print(li)