#定义函数:
def hanshu(a,b):
    return a+b
result=hanshu(2,6)
print(result)

#求圆的面积：
import math
def area(r):
    return math.pi*r*r
result=area(3)
print(result)

#def f(x):
 #   reversed x**2*3.14
#函数传入顺序：形参在实参的前面：eg:def(r,pi=3.14)。
#调用的时候可以加上定义的参数，也可以直接写值：eg:print(area(3))或者print(area(r=3))

#a=2
#ef main():
#  b=3
 #   print(a)
#main()
#print(b)  #b没有定义

#匿名函数：lambda
area=lambda r,pi:r*r*pi
print(area(3,3.14))

#用lambda求平均值：
s=[3,9,6]
n=list(map(lambda s:s/3,s))
print(n)

#不可更改对象:str,tuple,number
def f(a):
    a=10
b=2
f(b)
print(b)

#可更改对象：list,dict
c=[1,2,3]
def change(x):
    x.append([4,5,6])
change(c)
print(c)

#不定长参数：
def g(x,*y):
    print(x)
    for i in y:
        print(y)
g(1,2,3,4)
#元组是一个整体，不能用for i in遍历





    