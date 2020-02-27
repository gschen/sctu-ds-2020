def AplusB(a,b):
    c=a+b
    return c
    return a+b
result=AplusB(1,2)
print(result)
#计算圆的面积
def f(r):
    return 3.14*r*r
print(f(2))
#参数传递：传递顺序
#def circle(x=5.pi=3,14):
def circle(r,pi):
     area=r**2*pi
     return area
print(circle(6,3.14))
print(circle(pi=3.14,r=6))


#命名空间：全局变量、局部变量
a=2
def main():
    b=3
    print(a)
main()
print(b)
#匿名函数
circle=lambda r,pi:r**2*pi
print(circle(3,3.14))

#不可更改对象（传入的是对象的值）
def change(a):
    a=10
b=2
change(b)#b=a=10
print(b)
#可更改
c=[1,2,3]
# def change(x):
#     x.append([1,2,3])
change(c)
print(c)
#关键字参数
def printme(str):
    print(str)
    return
printme("关键字参数")
#不定长参数
# def main(x,*y):
#     print(x)
#     for x in y:
#         print(y)
# main(1,11,12,13,14)