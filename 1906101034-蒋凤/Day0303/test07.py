class parent():
    def __init__(self):
        self.p='我是父类'

    def f(self):
        print(self.p,'这是爸爸')
    
class child():
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self)