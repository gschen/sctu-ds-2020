#1、求给定数的阶乘,要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]

import math
list1=[1,10,20,30,40,50]
x=int(input('输入求阶乘的数：'))
if x not in list1:
    s=math.factorial(x)
print(s)