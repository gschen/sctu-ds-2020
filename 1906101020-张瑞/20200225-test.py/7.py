def AplusB(a,b):
    return a+b
result=AplusB(1,2)

def R(r):
    return r*r*3.14
print('面积为：',R(5))


a=10
b=20

circle=lambda r,pi:r**2*3.14
print(circle(3,3.14))

def C(a):
    a=10

b=2
C(b)
print(b)

d=[1,2,3]
def c(x):
    x.append([1,2,3])
c(d)
print(d)

def main(x,*y):
    print(x)
    print(y)
    for i in range(len(y)):
        print([i])
main(1,11,12,13,14)