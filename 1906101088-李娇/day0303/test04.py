class Test1():
    def __init__(self):
        self.x=[1,2,3] #实例变量
# a=Test()
# b=Test()
# a.x.append([1,2,3])
# print(a.x,b.x)

# c=list()
# d=list()
# c.append([1,2,3])


class Test2():
    x=[1,2,3] #类变量
a=Test1()
b=Test1()
a.x.append("abc")
print("Test01",a.x,b.x)

c=Test2()
d=Test2()
c.x.append("cde")
print("Test02",c.x,d.x)