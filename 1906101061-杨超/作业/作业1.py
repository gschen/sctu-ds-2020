# -*- coding: UTF-8 -*-
'''1、	求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
'''
x = int(input())
wrong_nums = [1,10,20,30,40,50]
def factorial(x):
    if x == 0:
        return "无意义"
    elif x == 1:
        return 1
    elif x in wrong_nums:
        print("不符要求")
    else:
        return x * factorial(x-1)
print (factorial(x))

'''2、	单利公式为：单利=（P x T x R）/ 100其中，P是本金T是时间，R是利率
例如输入：P = 10000
      R = 5
      T = 5
输出：2500
要求:P、T、R都是input输入的，不能固定。
'''
P = int(input('本金='))
R = int(input('时间='))
T = int(input('利率='))
单利=(P*T*R)/100
print("单利是{:.2f}".format(单利))

#3、	查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]。
nums = [14,25,98,75,23,1,4,56,59]
print(max(nums))

'''4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定。
'''
nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def pfh(x):
    return x*x
print(sum(map(pfh,nums[:n])))

'''5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
要求，被置换的两个位置需要input输入。
'''
a,b = map(int,input().split())
nums = [14,25,98,75,23,1,4,56,59]
num_a,num_b = nums[a],nums[b]
nums[b],nums[a] = num_a,num_b
print(nums) 
