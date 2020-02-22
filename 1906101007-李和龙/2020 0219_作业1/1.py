"""
1、	求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

"""

def Factorial(n):
    error_num = [1,10,20,30,40,50]
    if n < 0:
        return " have no"
    if n == 0 or n == 1:
        return 1
    else:
        return n*Factorial(n-1)
n = int(input())
error_num = [1, 10, 20, 30, 40, 50]
if n in error_num:
    print("error")
else:
    print(Factorial(n))


