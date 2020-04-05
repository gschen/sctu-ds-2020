#求圆的面积
def circle(r):
    return r**2*3.14
print(circle(5))


def circle(r,pi):
    area=r**2*pi
    return area
#area=circle(5,3.14)
#print(area)

area=circle(pi=3.14,r=5)
print(area)

#匿名函数
circle1=lambda r,pi:r**2*pi
print(circle(3,3.14))

#不可更改对象，只把对象的值传进去了
def change(a):
    a=10

b=2
change(b)
print(b)#结果为2

#可更改对象，传入的是对象本身
c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

#不定长参数
def main(x,*y):
    primt(x)
    print(y)
main(1,2,4,6,12)