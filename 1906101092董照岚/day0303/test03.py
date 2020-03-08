class Test1():
    def __init__(self):
        self.x=[1,2,3]#实列变量


class Test2():
    x=[1,2,3]#类变量

#test01
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

#test02
c=Test2()
d=Test2()
c.x.append('cde')
print('test02',c.x,d.x)
#类变量对所有对象都是公用的。