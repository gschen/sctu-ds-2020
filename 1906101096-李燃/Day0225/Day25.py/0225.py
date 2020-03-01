#函数
def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))




def circle(r):
    return r**2*3.14
print(circle(5))

#多个参数时，形参要在实参之前
def circle(r,pi=3.14):
    return r**2*3.14



#变量  全局变量，局部变量


#匿名函数 lambda
#格式  变量名=lambda参数1，参数2.....: 返回结果
circle1=lambda  r,pi:r**2*pi
print(circle1(3,3.14))

#不可更改对象（数字，字符串，元组）
def change(a):
    a=10

b=2
change(b)
print(b)


