class Test1():
    def __init__(self):
        self.t1='我是父类'
    def f(self):
        return '爸爸'
class Test2():
    def __init__(self):
        self.t2='我是子类'
    def f(self,object):
        print(object.f)
a=Test1()
b=Test2()
b.f(a)

def main(objict):
    print(object.f())

    return '123'
    