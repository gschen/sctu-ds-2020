class Test1():
    def __init__(self):
        self.t1 = "我是父亲"
    def f(self):
        return "爸爸"
class Test2():
    def __init__(self):
        self.t2 = "我是子类"
    def f(self, object):
        print(object.f())


a = Test1()




def main(object):
    print(object.f())
    return "q"


print(main(a))


#把类作为一个对象传入