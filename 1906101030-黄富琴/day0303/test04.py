class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量



class test2():
    x=[1,2,3]#类变量
#test01
a=Test1()
b=Test1()
a.x.append('abc')
print('Test01',a.x,b.x)

#test02
c=test2()
d=test2()
c.x.append('cdef')
print('test02',c.x,d.x)
