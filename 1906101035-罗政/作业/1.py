"""
1、	求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
"""
def s(n):
    if n ==1:
        return 1
    else:
        return n * s(n - 1)
n = int(input())
