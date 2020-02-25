"""
1、	求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

"""
def zxc(n):
    if n == 0:
        return 1
    else:
        return n zxc(n-1)
        print(zxc(20))