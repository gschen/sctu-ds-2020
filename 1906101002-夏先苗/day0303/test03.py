#类变量和实例变量
class Test1():
    def __init__(self):
        self.x=[1,2,3]


class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)
c=list()
d=list()
c.append([1,2,3])
