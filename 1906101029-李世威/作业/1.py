#1、	求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
list=[1,10,20,30,40,50]
a=int(input('请输入一个数:'))
def li(a):
    if a==0:
        return 1
    else:
        return a*li(a-1)
if a in list:
    print('此数不符合')
else:
    print(li(a))