#覆盖调用
class Test1():
    def __init__(self):
        self.t1='我是父亲'

    def f(self):
        print('这是爸爸')
class Test2(Test1):
    def __init__(self):
        self.t2='我是子类'
    def f(self):
        print('这是儿子')
a=Test2()
a.f()
super(Test2,a).f()