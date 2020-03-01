'''1、求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1，10，20，30，40，50]'''

x=int(input("请输入一个整数:"))
list=[1,10,20,30,40,50]
def jia(x):
    if x==0:
        return 1
    else:
        return x*jia(x-1)
if x in list or x<0 :
    print('不能输入此数！')
else:
    print(jia(x))

if x in list or x<0 :
    print('不能输入此数！')
else:
    for i in range(1,n+1):
        jjiecheng=1
        jiecheng=jiecheng*i
    print(jiecheng)
