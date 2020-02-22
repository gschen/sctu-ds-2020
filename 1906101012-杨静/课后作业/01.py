#求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

x = int(input("请输入一个整数："))
list=[1,10,20,30,40,50]
def yang(x):
    if x == 0:
        return 1
    else:
        return x*yang(x-1)
if x in list or x < 0:
    print('不能输入此数！')
    else:
        print(yang(x))