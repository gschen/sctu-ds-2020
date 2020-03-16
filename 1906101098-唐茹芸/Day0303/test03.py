#构造方法 （可以用来向类传参数）  类的实例化__init__


class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)

class Test():
    b=12
    def __init__(self):
        self.c = 12
a=Test()
print(a.b,a.c)



# class Test():
#     def __init__(self):
#         self.x=[1,2,3]
#     x = [1,2,3]
# a = Test()
# b = Test()
# a.x.append([1,2,3])
# print(a.x,b.x)


class Test1():
    def __init__(self):
        self.x=[1,2,3]  #实例变量

class Test2():
    x = [1,2,3]  #类变量 ,类变量在整个实例化的过程中是公用的

#test01
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

# test02
c=Test2()
d=Test2()
c.x.append('cde')
print('test02',c.x,d.x)