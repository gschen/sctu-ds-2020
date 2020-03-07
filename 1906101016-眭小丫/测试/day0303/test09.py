class Test1():
    def _init_(self):
        self.l1='我是父类'

    def f(self):
        return '爸爸'

class Test2():
    def _init_(self):
        self.t2='我是子类'

    def f(self,object):
        print(object.f())

a=Test1()

    # def main(object):
    #     print(object.f())
    #     return '123'
    # print(main(a))