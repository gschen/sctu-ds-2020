#构造方法 __init__()
#1.
class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)
b=list([1,2,3])
print(b)

#2.
class Test():
    a=12
    def __init__(self,a=a):
        print(a)
a=Test()#类不可以传参

#3.
class Test():
    b=12
    def __init__(self):
        self.c=12#定义实例变量
a=Test()
print(a.b,a.c)

#4.
class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)

class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3]) #类变量在实例化中都是公用的
print(a.x,b.x)      #b会受到影响

#5.
class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量，b不受到影响
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)

#实例变量与类变量的区别
# 实例变量:属于实例化的对象
# 类变量:在整个实例化对象中都是公用的
# 一般使用类变量，实例变量容易出错
class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量

class Test2():
    x=[1,2,3]#类变量
#test01
a=Test()
b=Test()
a.x.append('abc')
print('test01',a.x,b.x)
#test02
c=Test()
d=Test()
c.x.append('cde')
print('test02',c.x,d.x)