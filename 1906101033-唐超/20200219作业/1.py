#1、	求给定数的阶乘
#       要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
x=int(input())
for i in range(1,x):
    x*=i
print(x)