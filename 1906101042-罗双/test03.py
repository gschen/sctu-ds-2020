class Myclass:
    """一个简单的类实例"""
    i=12345
    def f(self):
        return 'hello world' #实例化类
x=Myclass() #访问类的属性和方法
print("Myclass类的属性i为：",x.i)
print("Myclass类的方法f输出为：",x.f())


#实现一个Test类，包括original和overturn两个方法
#original方法从a到z打印26个小写英文字母
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]:
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()


#构造方法（__init__()）
class Test():
    def __init__(self,a,b):
        print("已运行",a+b)
a=Test(10,20)
b=list([1,2,3])
print(b)


#类变量和实例变量区别
#类变量：
class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)

#s实例变量
class Test():
    def __init__(self):
        self.x=[1,2,3]

a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)


#类的继承（当子类方法与父类方法重名，优先调用子类中的方法；在继承多个父类时，调用父类方法会从左至右依次检索每个父类中是否有该方法）
class Parent():
    def __init__(self):
        self.p='我是父类'
    def f(self):
        print(self.p,'财产1w')
class Child(Parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')
a=Child()
a.t()
a.f()


#私有公有
class Test:
    def __init__(self):
        self.__x=1
        self.y=2
    def __f(self):
        print('这是密码')
a=Test()
print(a,y)

a.f()
a.__f()


#类作为参数传递
class Test1():
    def __init__(self):
        self.t1='父类'
    def f(self):
        return '爸爸'
class Test2():
    def __init__(self):
        self.t2='子类'
    def f(self,object):
        print(object,f())
a=Test1()
b=Test2()
b.f(a)

def main(object):
    print(object,f())
    return '123'
print(main(a))
