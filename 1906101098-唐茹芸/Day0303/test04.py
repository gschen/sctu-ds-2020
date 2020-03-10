
# 类的继承

# 一个类可以通过继承获取另一个类的方法，但不能继承属性


class parent():
    def __init__(self):
        self.p='我是父类'
    def f(self):
        print('财产100万')
class child(parent):
    def  __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')
a=child()
a.t()
a.f()
super(child,a).f()  #覆盖调用