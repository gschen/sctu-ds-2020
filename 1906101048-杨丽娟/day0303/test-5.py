class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量



class Test2():
    x=[1,2,3]#类变量
#test01
a=Test1()
b=Test2()
a.x.append('abc')
print('test1',a.x,b.x)

#test2
c=Test2()
d=Test2()
c.x.append('cde')
print('test2',c.x,d.x)