#给定数阶乘 要求：所有阶乘不可以是：[1，10，20，30，40，50]
def jc(n):
    a=1
    b=[1,10,20,30,40,50]
    if a <n:
         for i in range(1,n+1):
                 a= a*i
    if n in b:
        print('none')
    else:
        print(a)
n=eval(input("请放入一个数："))
jc(n)