#求给定数的阶乘(要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50])
n=eval(input('请输入一个非负整数:'))
a=1
if n==1 or n==10 or n==20 or n==30 or n==30 or n==40 or n==50:
    print('不能输入这个数')
elif n==0:
    print(1)
else:
    for i in range(1,n+1):
        a=a*i
    print(a)