class Test():
    def __init__(self):
        print('已运行',a+b)
    a=Test(10,20)

class Test1():
    x=[1,2,3]#实例变量
a=Test()
b=Test()
a.x.append('abc')
print('test1',a.x,b.x)
class Test2():
    x=[1,2,3]#类变量
c=Test2()
d=Test2()
c.x.append('cde')
print('test2',c.x,d.x)





