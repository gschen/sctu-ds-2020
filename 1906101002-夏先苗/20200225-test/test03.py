def AplusB(a,b):
    c=a+b
    return c
result=AplusB(1,2)
print(result)


#传入r,计算圆的面积
def circle(r):
    return r**2*3.14
print(circle(5))

def circle2(r):
    area=r**2*3.14
    pi=3.1415926
    return area,pi
print(circle2(5))



def aplusb(a,b):
    return a+b
result=aplusb(1,2)
print(result)
print(aplusb(10,12))


def circle3(r,pi):
    area=r**2*pi
    return area
print(circle3(6,3.1415926))

circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))


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

