# class MyClass:
#     i = 12345  #类变量
#     def f(self):
#         return "hello,world"  #实例化类
# x = MyClass()  #创建一个MyClass类的对象x
# print("MyClass 类的属性i为：",x.i)  # x.i 访问对象属性即类变量
# print("MyClass 类的方法f输出为：",x.f())


# class Test():
#     def original(self):
#         lis = [chr(i) for i in range(97,123)]    #97-122是ACSII码对应小写字母a-z
#         # print(lis)
#         print(''.join(lis))
#     def overturn(self):
#         li = (chr(i) for i in range(90,64,-1))   #65-90是ACSII码对应大写字母A-Z
#         print(''.join(li))  
# a = Test()
# a.original()
# a.overturn()


# class Test():
#     def __init__(self,a,b):
#         print('已运行',a+b)
# a=Test(10,20)

# class Test():
#     b=12
#     def __init__(self):
#         self.c = 12
# a=Test()
# print(a.b,a.c)



# class Test():
#     def __init__(self):
#         self.x=[1,2,3]
#     # x = [1,2,3]
# a = Test()
# b = Test()
# a.x.append([1,2,3])
# print(a.x,b.x)



# #类变量、实例变量
# class Test1():
#     def __init__(self):
#         self.x=[1,2,3]  #实例变量

# class Test2():
#     x = [1,2,3]  #类变量 ,类变量在整个实例化的过程中是公用的

# #test01
# a=Test1()
# b=Test1()
# a.x.append('abc')
# print('test01',a.x,b.x)

# # test02
# c=Test2()
# d=Test2()
# c.x.append('cde')
# print('test02',c.x,d.x)



# # 类的继承
# # 一个类可以通过继承获取另一个类的方法，但不能继承属性
# class parent():
#     def __init__(self):
#         self.p='我是父类'
#     def f(self):
#         print('财产100万')
# class child(parent):
#     def  __init__(self):
#         self.c='我是子类'
#     def t(self):
#         print(self.c,'我要继承')
# a=child()
# a.t()
# a.f()
# # super(child,a).f()



# # 私有公有
# class Test:
#     def __init__(self):
#         self.__x=1
#         self.y=2

#     def __f(self):
#         print('这是密码')
# a=Test()
# print(a.y)
# print(a.x,a.__x) #无法调用



# #类作参数
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

# def main(object):
#     print(object.f())
#     return '123'
# print(main(a))





# #类的标准写法
# class Myclass():
#     def __init__(self,a,b):#实例化时传入参数
#         #定义变量
#         self.x=a
#         self.y=b
#         #self.xxx........
#         #也可以写一些在实例化时便要执行的操作

#     #定义函数往后
#     def f1(self):
#         #如果要调用实例变量 --> self.变量名
#         c=self.x+self.y
#         return c
#     def f2(self):
#         pass