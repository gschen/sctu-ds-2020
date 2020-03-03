# 构造方法_init_()
class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)

# 类变量和实例变量 实例变量用得较多
# class Test():
#     x=[1,2,3]
# a=Test()
# b=Test()
# a.x.append(['abc'])
# print(a.x,b.x)



class Test1():
    def __init__(self):
        self.x=[1,2,3] #实例变量

class Test2():
    x=[1,2,3]#类变量
# test01
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

# test02
c=Test2()
d=Test2()
c.x.append('cde')
print('test02',c.x,d.x)

