class parent():
    def __init__(self):
        self.p='我是父亲'
    
    def f(self):
        print('财产1w')

class child(parent):
    def __init__(self):
        self.c='我是子类'
    def f(self):
        print(self.c,'我要继承')


a=child()
a.f()


