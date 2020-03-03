a=2
def main():
    b=3
    print(a)
main()
print(b)

circle2=lambda r,pi:r**2*pi
print(circle2(3,3,14))

def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(ApulsB(10,12))

def circle(r,pi):
    area=r**2*pi
    return are
print(circle(6,3.1415926))
peint(circle(pi=3.1415926))



a=2
def main():
    b=3
    print(a)
main()
print(b)#全集变量，b是错的


#匿名函数
circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))


def change(a):#不可更改对象
    a=10
b=2
change(b)#2->a,a=2->a=10
print(b)

#可更改对象
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