# class Test():
#     list_ot=[]
#     x=1
#     def __init__(self):
#         self.lis_in=[]

# class Myclass():
#     i=123456
#     def f(self,Ostr):
#         print(Ostr)
# x=Myclass()
# print(x.i,x.f('wo'))




# class Test():
#     def original(self):
#         lis=[chr(i) for i in range(97,123)]
#         print(''.join(lis))
#     def overturn(self):
#         lis1=[chr(i) for i in range(90,64,-1)]
#         print(''.join(lis1))
# a=Test()
# a.original()
# a.overturn()



# class Test():
#     def __init__(self,a,b):
#         print('已经运行',a+b)
# a=Test(10,20)



# class Test():
#     a=12
#     def __init__(self,a=2):
#         print(a)


# class Test():
#     b=12
#     def __init__(self):
#         self.c=12
# a=Test()
# print(a.b,a.c)


#l类变量
# class Test():
#     x=[1,2,3]#(对于字符串是没用的，数字也一样)
# a=Test()
# b=Test()
# a.x.append([1,2,3])
# print(a.x,b.x)
# 实例变量
# class Test():
#     def __init__(self):
#         self.x=[1,2,3]
# a=Test()
# b=Test()
# a.x.append([1,2,3])
# print(a.x,b.x)




# #类的标准写法
# class Myclass():
#     def  __init__(self,a,b):
#         #定义变量在此处
#         self.x=a
#         self.y=b
#         #self.x....
#         #也可以这样写一些在实例化时便要执行的操作

#     #定义函数后
#     def f1(self):
#         #如果要调用实例变量
#         c=self.x+self.y
#         return c
#     def f2(self):
#         pass
#     #0000





# class parent():
#     def __init__(self):
#         self.p='我是你爸爸'
#     def f(self):
#         print('财产1w')
# class son(parent):
#     def __init__(self):
#         self.c='我是儿子'
#     def t(self):
#         print(self.c,'我要继承你的财产')
# a=son()
# a.t()
# a.f()
# super(son,a).f()




#在函数前加__就无法让别人调用
# class Test():
#     def __init__(self):
#         self.__x=1
#         self.y=2
#     def __f(self):
#         print('这是密码')
# a=Test()
# print(a.y)
# a.f()
# a.__f()


# 类做为参数
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