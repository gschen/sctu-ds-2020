lass parent():
    def __init__(self):
        self.p="我是父亲"

    def f(self):
        print("财产1万")
class child(parent):
    def __init__(self):
        self.c="我是儿子"
    def t(self):
        print(self.t,"我要继承")  
a=child()
a.t()
a.f()