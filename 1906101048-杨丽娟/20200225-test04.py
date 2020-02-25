def AplusB(a,b):

    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))



def circle(r):
    return r**2*3.14
print(circle(4)) 





a=2
def main():
    print(a)
main()
print(a)


circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))


def change(a):
    a=10


b=2
change(b)#2->a,a=2->a=10
print(b)


c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)



b='123'
b=123
