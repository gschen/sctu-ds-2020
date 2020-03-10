class MyClass(): #不加“()”也能运行
    i=123456
    def f(self,ostr):
        print(ostr)
x=MyClass()
print(x.i,x.f('hello,word'))

#
class Test(): #类名要大写
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
a=Test()
a.original()

#
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
    def overturn(self):
        print('',join([chr(i) for i in range(65,91)]))
a=Test()
a.original()

#
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
    def overturn(self):
        print('',join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()


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
a=Test() #类不可以传参

#3.
class Test():
    b=12
    def __init__(self):
        self.c=12 #定义实例变量
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
        self.x=[1,2,3] #实例变量，b不受到影响
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)

#实例变量与类变量的区别
#实例变量:属于实例化的对象
#类变量:在整个实例化对象中都是公用的
#一般使用类变量，实例变量容易出错
class Test1():
    def __init__(self):
        self.x=[1,2,3] #实例变量

class Test2():
    x=[1,2,3] #类变量
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

#类的标准写法
class Myclass():
    def __init__(self,a,b):#实例化时传入参数在这
        #定义变量在此处
        self.x=a
        self.y=b
        #self.xxx.....
        #也可以写一些在实例化时便于执行的操作

    #定义函数往后
    def f1(self):
        #如果要调用实例变量-->self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass


#类的继承
class parent():
    def __init__(self):
        self.p='我是父类'

    def f(self):
        print('财产100w')

class child(parent): #可以有多个“父亲”
    def __init__(self):
        self.c='我是子类'
    def t(self):   #def f(self):会将前面的覆盖
        print(self.c,'我要继承')

a=child()
a.t()
a.f()

#私有与公有
class Test:
    def __init__(self):
        self.__x=1 #私有变量，不能调用
        self.y=2 #公有变量

    def __f(self): #私有函数
        print('这是密码')

a=Test()
print(a.y)
print(a.__x)
a.f()
a.__f()
