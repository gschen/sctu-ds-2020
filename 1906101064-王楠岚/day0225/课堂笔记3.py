#函数
def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)

def circle(r):
    return r**2*3.14
print(circle(5))

def circle(r=6):
    a=r**2*3.14
    return a
print(circle(r=6))
#a=2，b未被定义
a=2
def main():
    b=3
    print(a)
main()
print (b)
#lambda
circle3=lambda r,p:r**2*p
print(circle3(3,3.14))

def change(a):
    a=10

b=2
change(b)#b=a=10
print(b)
#字符串，元组不可更改
c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

def main (x,*y):
    print(x)
    print(y)
main(1,11,12,13,14)
