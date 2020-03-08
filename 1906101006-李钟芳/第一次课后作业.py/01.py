#1、求给定数的阶乘  要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

x = int(input())
wrong_nums = [1,10,20,30,40,50]
def li(x):
    if x == 0:
        return 1
    else:
        return x*li(x-1)
if x in wrong_nums:
    print('不能输入此数')
else:
    print(li(x))