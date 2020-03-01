def A(a,b):
    c=a+b
    return c
result=A(1,2)
print(result)

def A(a,b):
    return a+b
result=A(1,2)
print(result)

#传入r，计算圆的面积
def circle(r):
    return 3.14*r**2
print(circle(2))

def circle(r):
    s=3.14*r**2
    pi=3.1415926
    return s,pi
print(circle(2))


def A(a,b):
    return a+b
#result=A(1,2)
#print(result)
print(A(1,2))

def ciccle(r,pi):
    s=r**2*pi
    return s
print(circle(3,3.14))



circle=lambda r,pi:r**2*pi                  #Lambda函数：def 函数的单行写法
print(circle(2,3.14))                       #格式：变量名 = lambda 参数1,参数2… : 返回结果


def change(a):
    a=5                                #而 list,dict 等则是可以修改的对象strings, tuples, 和 numbers 是不可更改的对象
b=2                                    #传入不可更改对象,函数在传入不可更改对象时传入的是该对象的值，而不是这个对象本身。
change(b)
print(b)



c=[1,2,3]
def change(x):
    x.append([1,2,3])
    change(c)
print(c)


b='1,2,3'
b=123
def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
main(1,11,12,13,14,15)