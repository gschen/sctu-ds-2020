class Test1:
    def __init__(self):
        self.t1='我是父类'
    def f(self):
        return '爸爸'

class Test2:
    def __init__(self):
        self.t2='我是子类'
    def f(self,object):
        print('这是我',object.f())

a=Test1()
b=Test2()
b.f(a)