#类中定义的函数，第一个参数必须是self
class Myclass:
    i=134
    def f(self):
        return 'hello,world'
x=Myclass()
print('Myclass类的属性i为：',x.i)
print('Myclass类的方法f的输出为：',x.f())


#用类实现a-z的打印以及A-Z的逆序打印
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(lis)
    def overturn(self):
        lis2=[''.join(chr(j) for j in range(90,64,-1))]
        print(lis2)
a=Test()
a.original()
a.overturn()

#类变量和实例变量统称为属性
#构造方法：__init__
class Test():
    def __init__(self):
        print(0)
    def f(self):
        print(1)
b=Test()
#构造方法在类实例化时便执行，可以用来向类中传入参数
class Test():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def f(self):
        print(self.x+self.y)
m=Test(3,4)

#类变量和实例变量的区别：
#类变量
class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)
#实例变量
class Test():
    def __init__(self):
        self.x=[1,2,3]
a=Test()
b=Test()
a.x.append(['cde'])
print(a.x,b.x)

#类的继承：一个类可以通过继承获取另一个类的方法
class Test():
    def __init__(self):
        self.t1='我是父类'
    def f(self):
        print('这是爸爸')
class Test2(Test):
    def __init__(self):
        self.t2='我是子类'
    def t(self):
        print('这是儿子')
a=Test2()
a.t()
a.f()
print(a.t2)      

#公有私有
class Test():
   # __secret=0
    public=10
    def count(self):
       # self.__secret+=1
        self.public+=1
       # print(self.__secret)
counter=Test()
counter.count()
counter.count()
#print(counter.__secret)
print(counter.public)

#对象作为参数传递
class Test():
    def __init__(self):
        self.t1='我是父类'
    def f(self):
        return 'father'
class Test2():
    def __init__(self):
        self.t2='我是子类'
    def f(self,object):
        print('this is my good',object.f())
b=Test()
a=Test2()
a.f(b)
