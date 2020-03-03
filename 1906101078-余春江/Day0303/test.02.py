#类的继承
class parent():
    def __init__(self):
        self.p='我是父类'

    def f(self):
        print('财产1W')

class child(parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.t()
a.f()