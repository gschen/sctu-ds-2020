#类的继承
class parent():
    def __init__(self):
        self.p='我是父类'

    def f(self):
        print('财产1w')

class child(parent1,parent2):#()内可有多个父亲
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.t()
a.f()


#方法重写：子类与父类函数同名
class parent():
    def __init__(self):
        self.p='我是父类'

    def f(self):
        print('财产1w')

class child(parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.f()
super(child,a).f()#覆盖调用

#私有与公有
class Test:
    def __init__(self):
        self.__x=1#私有变量，不能调用
        self.y=2#公有变量

    def __f(self):#私有函数
        print('这是密码')

a=Test()
print(a.y)
a.f()

#类作为参数传递
class Test1():
    def __init__(self):
        self.t1='我是父类'

    def f(self):
        return '父'

class Test2():
    def __init__(self):
        self.t2='我是子类'

    def f(self,object):#object用于传入参数，为一个类
        print(object.f())

a=Test1()
b=Test2()

def main(object):
    print(object.f())#把一个对象作为参数传到函数里