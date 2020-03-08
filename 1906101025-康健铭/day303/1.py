# class MyClass:
#     i = 12345
#     def f(self, ostr):
#         return ostr


# x = MyClass()
# print(x.i, x.f("hello, world"))



# class Test():
#     def original(self):
#         lis = [chr(i) for i in range(97, 123)]
#         print(",".join(lis))
#     def overturn(self):
#         print(','.join([chr(i) for i in range(90, 64, -1)]))


# a = Test()
# a.original()
# a.overturn()


# class Test():
#     a = 1
#     def __init__(self, a = a):
#         print("已经运行", a+b)    类变量

# a = Test(10, 20)

# class Test():
#     x = [1, 2, 3]
# a = Test()
# b = Test()
# a.x.append([1, 2, 3])
# print(a.x, b.x)



# 实例变量
# class Test():
#     def __init__(self):
#         self.x = [1, 2, 3]
# a = Test()
# b = Test()
# a.x.append([1, 2, 3])
# print(a.x, b.x)




# 继承
# class parent():
#     def __init__(self):
#         self.p = "我是父亲"
#     def f(self):
#         print('这是爸爸')

# class child(parent):
#     def __init__(self):
#         self.c = "我是子类"
#     def t(self):
#         print(self.c, "我要继承")

# a = child()
# a.t()
# a.f()

# class parent():
#     def __init__(self):
#         self.p = "我是父亲"
#     def f(self):
#         print('财产')

# class child(parent):
#     def __init__(self):
#         self.c = "我是子类"
#     def f(self):
#         print(self.c, "我要继承")

# a = child()
# a.f()
# super(child,a).f()




# class Test:
#     def __init__(self):
#         self.__x = 1
#         self.y = 2
#     def __f(self):
#         print("这是密码")

# a = Test()
# print(a.y)





# class Test1():
#     def __init__(self):
#         self.t1 = "我是父亲"
#     def f(self):
#         return "爸爸"
# class Test2():
#     def __init__(self):
#         self.t2 = "我是子类"
#     def f(self, object):
#         print(object.f())


# a = Test1()




# def main(object):
#     print(object.f())
#     return "q"


# print(main(a))


#把类作为一个对象传入