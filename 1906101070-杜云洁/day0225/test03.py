#Python函数
#函数语法
def ApulsB(a,b):
    return a+b
result=ApulsB(1,2)
print(result)
print(ApulsB(1,2))
#实例：求圆的面积
def circle(r):
    return 3.14*r**2
print(circle(6))
def circle(r):
    s=3.14*r**2
    pi=3.14
    return pi,r,s
pi,r,s=(circle(6))
print(pi,r,s)

#参数传递
#参数传递顺序(形参在实参之前)
def circle(r=6,pi=3.14):
    s=3.14*r**2
    pi=3.14
    return s,pi
s,pi=circle()
print(pi,s)
def circle(r,pi):
    s=pi*r**2
    return s
print(circle(6,3.14))
print(circle(r=6,pi=3.14))


#命名空间
#全局变量：全局空间定义的变量
# a=10
# b=20
# #局部变量：函数等局部空间里面定义的变量
# a=2#(全局变量)
# def main():
#     b=3#(局部变量)
#     print(a)
# main()
# print(b)
#局部空间可以访问全局变量
#全局空间不可访问局部变量

#匿名函数:lambda
circle=lambda r,pi:r**2*pi
print(circle(6,3.14))
#传可更改对象与不可更改对象
#不：字符串，数字，元祖 (函数传入的是该对象的值)
def change(a):
    a=10
b=2
change(b)
print(b)   
#可：列表，字典,集合(函数传入的是该对象本身)
c=[1,2,3]
def change(x):
    x.append([1,2,3])
change(c)
print(c)
#关键字参数
def hi(str):
    print(str)
    return
hi(str='hello')
#不定长参数
def main(x,*y):
    print(x)
    print(y)
main(1,11,12,13,14)
