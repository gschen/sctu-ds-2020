class Test1():
    def __int__(self):
        self.t1="我是父类"

    def f(self):
        return "爸爸"
class Test2():
    def __init__(self):
        self.t2="我是子类"

    def f(self,pbject):
        print(object.f())#object以对象传入

a=Test1()
b=Test2()
b.f(a)
