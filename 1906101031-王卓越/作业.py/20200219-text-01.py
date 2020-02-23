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

