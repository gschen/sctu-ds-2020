class parent():
    def _init_(self):
        self.p='我是父类'
    
    def f(self):
        print('财产1w')

class child():
    def _init_(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.t()
a.f()