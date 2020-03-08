class Test:
    def __init__(self):
        self._x-1
        self.y=2
    def __f(self):
        print('这是密码')


class Test1():
    def __init__(self):
        self.t1='我是父类'

    def f(self):
        return '爸爸'
class Test2(Test1):

    def __init__(self):
        self.t2='我是子类'
    def f(self,object):
         print('这是我',object.f())
b=Test1()
a=Test2()
a.f(b)