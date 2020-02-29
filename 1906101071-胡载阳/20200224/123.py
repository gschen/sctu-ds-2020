




















circle2=lambda r,pi:r**2*pi
print(ciecle2())





def circle(r):
    area=r**2*3.14
    pi=3.1415926
    return area,pi

area,pi=circle(5)
print(pi,area)


a=2
def main():
    b=3
    print(a)
main()
print(b)

circle3=lambda r,pi:r**2*pi
print(circle(3,3,14))


def change(a):
    a=10

b=2
change(b)#2->a,a=2->a=10
print(b)

c=[1,2.3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

b='123'
b=123

def main(x,*y):
    print(x)
    print(y)

main(1,11,12,13,14)



