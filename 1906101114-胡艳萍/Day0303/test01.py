# 类
# 标准写法：
class Myclass():
    def __init__(self,a,b):
        # 定义变量
        self.x=a
        self.y=b
        # self.xxx....
        # 也可以写一些在实例化时便要执行的操作

    # 定义函数往后
    def f1(self):
        # 如果要调用实例变量--> self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass

# class MyClass():
#     i=12345
#     def f(self,ostr):
#         print(ostr)
# x=MyClass()
# print(x.i,x.f('hello,world'))

# class Test():
#     def original(self):
#         lis=[chr(i) for i in range(97,123)]
#         print(''.join(lis))
#     def overturn(self):
#         print(''.join([chr(i) for i in range(65,91)]))
# a=Test()
# a.original()
# a.overturn()

# class Test():
#     def __init__(self,a,b):
#         print('已运行',a+b)
# a=Test(10,20)

# 类变量：
# class Test():
#     x=[1,2,3]
# a=Test()
# b=Test()
# a.x.append([1,2,3])
# print(a.x,b.x)

# 实例变量：
# lass Test():
#     def __init__(self):
#         self.x=[1,2,3]
# a=Test()
# b=Test()
# a.x.append([1,2,3])
# print(a.x,b.x)

# 类的继承:一个类可以通过继承获取另一个类的方法
# class parent():
#     def __init__(self):
#         self.p='我是父类'
#     def f(self):
#         print('财产1w')
# class child(parent):
#     def __init__(self):
#         self.c='我是子类'
#     def t(self):
#         print(self.c,'我要继承')
# a=child()
# a.t()
# a.f()

# 私有公有
# class Test:
#     def __init__(self):
#         self.__x=1
#         self.y=2
#     def __f(self):
#         print('这是密码')
# a=Test()
# print(a.y)

# 类作参数
# class Test1():
#     def __init__(self):
#         self.t1='我是父类'
#     def f(self):
#         return '爸爸'
# class Test2():
#     def __init__(self):
#         self.t2='我是子类'
#     def f(self,object):
#         print(object.f())
# a=Test1()
# b=Test2()
# b.f(a)