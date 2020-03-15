class Test():
    def __init__(self):
        self.t1='我是父亲'

    def f(self):
        return'爸爸'
    
class Test2():
    def __init__(self):
        self.t2='我是子类'

    def f(self,object):
        print(object.f())

a=lest1()

def main (object):
    print(main())