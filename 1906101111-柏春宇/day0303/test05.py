class Parent():
    def __init__(self):
        self.p='我是父类'
    
    def f(self):
        print('财产一W')

class Child(Parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=Child()
a.t()
a.f()
