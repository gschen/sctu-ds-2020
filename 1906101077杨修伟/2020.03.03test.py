# class Myclass:
#     i=123456
#     def f(self,ostr):
#         return ostr
# x=Myclass()
# print(x.i,x.f('hello,world'))


# class Test():
#     def original(self):
#         L=[chr(i) for i in range(97,123)]
#         print(''.join(L))
#     def overturn(self):
#         print(''.join([chr(i) for i in range(90,64,-1)]))
# a=Test()
# a.original()
# a.overturn()


# class Test():
#     def __init__(self,a,b):
#         print('已运行',a+b)
# a=Test(1,2)


# class Test1():
#     x=[1,2,3]      #类变量
# class Test2():
#     def __init__(self):      #实际变量
#         self.x=[1,2,3]
# a=Test1()
# b=Test1()
# a.x.append('abc')
# print('test1:',a.x,b.x)
# c=Test2()
# d=Test2()
# c.x.append('yxw')
# print("tsst2:",c.x,d.x)



# class Parent():
#     def __init__(self):
#         self.p='我是父亲'
    
#     def f(self):
#         print('财产一万')
    
# class Child(Parent):
#     def __init__(self):
#         self.c='我是子类'
#     def t(self):
#         print(self.c,'我要继承')
# a=Child()
# a.t()
# a.f()


# class Parent():
#     def __init__(self):
#         self.p='我是父亲'
    
#     def f(self):
#         print('财产一万')
    
# class Child(Parent):
#     def __init__(self):
#         self.c='我是子类'
#     def f(self):  #覆盖了父类的f
#         print(self.c,'我要继承')
# a=Child()
# a.t()
# a.f()



# class Test():
#     def __init__(self):
#         self.__x=1
#         self.y=2
#     def __f(self):
#         print("这是密码")
# a=Test()
# print(a.y)
# a.__f()


class Test01():
    def __init__(self):
        self.t1='我是父类'
    def f(self):
        return '爸爸'
class Test02():
    def __init__(self):
        self.t2='我是子类'
    def f(self,object):
        print(object.f())
a=Test01()
def main(object):
    print(object.f())
    return '123'
print(main(a))