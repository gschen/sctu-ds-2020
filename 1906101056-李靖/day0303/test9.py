class parent():
    def __int__(self):
        self.p='我是父类'
    def f(self):
        print(self.p,'财产1w')
class child(parent):
    def __int__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.t()
a.f()