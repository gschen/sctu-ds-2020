#1、	求给定数的阶乘  
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]

n = int(input('请输入一个整数:'))
list = [1,10,20,30,40,50]
def fg(n):
    if n==0:
        return 1
    else:
        return n*fg(n-1)
if n in list or n<0:
    print('此数不可以输入！')
else:
    print(fg(n))