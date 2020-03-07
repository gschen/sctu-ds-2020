# 类做参数
class Test1():
    def __init__(self):
        self.t1='我是父类'
    
    def f(self):
        return'爸爸'
class Test2(Test1):
    def __init__(self):
        self.t2='我是子类'
    
    def f(self,object):
        print(object.f())
b=Test1()
a=Test2()
a.f(b)