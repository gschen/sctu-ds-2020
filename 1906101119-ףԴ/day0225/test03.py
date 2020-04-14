def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))

def circle(r):
    area=r**2*3.14
    return area
print(circle(5))

def circle2(r,pi):
    area=r**2*pi
    return area
print(circle2(6,3.14))

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
print(a)

c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
main(1,11,12,12,13)