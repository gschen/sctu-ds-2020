def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))

def circle(r):
    return r**2*3.14
print(circle(5))


a=2
def main():
    b=3
    print(a)
main()
print(b)


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


def printinfo(arg1,*vartuple):
    "打印任何传入的数字"
    print("输出：")
    print(arg1)
    print(vartuple)
printinfo(70,60,50)