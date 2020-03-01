#求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]

list=[1,10,20,30,40,50]
n=int(input('请输入一个数：'))
factorial = 1
if n < 0:
    print('负数没有阶乘')
elif n == 0:
    print(1)
else:
    if n in list:
        print('错误')
    else:
        for i in range(1,n+1):
            factorial = factorial*i
        print('%d 的阶乘为 %d'%(n,factorial))
