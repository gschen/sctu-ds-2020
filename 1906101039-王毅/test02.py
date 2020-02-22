#求给定数的阶乘
x = int(input())
b = [1,10,20,30,40,50]
def jiecheng(x):
    if x == 0:
        return 1
    else:
        return x*jiecheng(x-1)
if x in b：
    print('wrong')
else:
    print(jiecheng(x))

#2	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
#例如输入：P = 10000
  #    R = 5
  #    T = 5
#输出：2500
#要求:P、T、R都是input输入的，不能固定.
P,T,R = map(int,input().split())
def gs(P,T,R):
    return (P*T*R)/100
print(gs(P,T,R))

#查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]
print(max([14,25,98,75,23,1,5,56,59]))
#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def jiang(x):
    return x*x
print(sum(map(jiang,nums[:n])))
#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入



