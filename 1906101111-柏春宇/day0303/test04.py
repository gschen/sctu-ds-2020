class Test1():
    def __init__(self):
        self.x=[1,2,3]
a=Test1()
b=Test1()
a.x.append(['abc'])
print(a.x,b.x)#实例变量


class Test2():
    x=[1,2,3]
c=Test2
d=Test2
c.x.append(['cde'])
print(c.x,d.x)#类变量