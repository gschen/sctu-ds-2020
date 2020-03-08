#私有公有

class Test():
    def __init__(self):
        self.__x=1
        self.y=2
    def __f(self):
        print("这是密码")
a=Test()
print(a.y)

a.f()
a.__f()


#类作参数

class Test1():
    def __init__(self):
        self.t1="我是父类"

    def f(self):
        return "爸爸"

class Test2():
    def __init__(self):
        self.t2="我是子类"

    def f(self,object):
        print(object.f())
a=Test1()
b=Test2()
b.f(a)