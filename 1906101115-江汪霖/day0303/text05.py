class Test():
    def __init__(self):
        self.x=[1,2,3]  #实例变量



class Test2():
    x=[1,2,3]  #类变量

a=Test()
b=Test()
a.x.append("abc")
print("text",a.x,b.x)


c=Test2()
d=Test2()
c.x.append("cde")
print("test2",c.x,d.x)