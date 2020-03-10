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
super(child,a).f() #覆盖调用