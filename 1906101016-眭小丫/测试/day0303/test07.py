class parent():
    def _init_(self):
        self.p='我是父类'

    def f(self):
        print('财产1w')

class child(parent):
    def _init_(self):
        self.c='我是子类'
    def f(self):
        print(self.c,'我要继承')

a=child()

a.f()


