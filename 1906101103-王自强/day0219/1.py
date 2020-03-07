'''1、求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]'''
x = int(input())
wrong_nums = [1,10,20,30,40,50]
def jiang(x):
    if x == 0:
        return 1
    else:
        return x*jiang(x-1)
if x in wrong_nums:
    print('wrong num')
else:
    print(jiang(x))