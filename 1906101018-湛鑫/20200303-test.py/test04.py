#类作为参数传递
class Test1:
    def __init__(self):
        self.t1='我是父类'
    def f(self):
        return '爸爸'

class Test2:
    def __init__(self):
        self.t2='我是子类'
    def f(self,object): #object用于传入参数，作为一个类
        print('这是我',object.f())

a=Test1()
b=Test2()
b.f(a)

def main(object):
    print(object.f()) #把一个对象作为参数传到函数里