#函数
#语法

def AplusB(a,b):
    c=a+b
    return c
result=AplusB(1,2)
print(result)


#实例1 传入r,计算圆的面积
def circle(r):
    return r**2*3.14
print(circle(5))

def circle2(r):
    area=r**2*3.14
    pi=3.1415926
    return area,pi

area,pi=circle2(5)
print(pi,area)

#传入参数(形参，实参)(形参在实参前面)

def circle3(r,pi):
    area=r**2*pi
    return area
print(circle3(6,3.1415926))

circle3=lambda r,pi:r**2*pi  #匿名函数lambda
print(circle3(3,3.14))
'''传可更改对象与不可更改对象
定义：
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
传入不可更改对象
函数在传入不可更改对象时传入的是该对象的值，而不是这个对象本身'''
def change(a):
    a=10
b=2
change(b)
print(b)

c=[1,2,3]
def change2(x):
    x.append([1,2,3])
    change2(c)
    print(c)



b='123'
b=123

def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
main(1,11,12,13,14)
