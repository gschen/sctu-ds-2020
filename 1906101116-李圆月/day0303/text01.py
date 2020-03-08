# class MyClass():
#     i=1234556
#     def f(self,ostr):
#         print(ostr)
# x=MyClass()
# print(x.i,x.f('hello,world'))


# class Test():
#     def original(self):
#         lis=[chr(i)for i in range(97,123)]
#         print(''.join(lis))
#     def overturn(self):
#         print(''.join([chr(i) for i in range(90,64,-1)]))
# a=Test()
# a.original()
# a.overturn()

# class Test():
#     def _int_(self):
#         print('已运行')
# a=Test(10,20)
# b=list([1,2,3])
# print(b)


# class Test():
#     a=12
#     def _init_(self,a=a):
#         print(a)
# a=Test()
# class Test():
#     b=12
#     def _init_(self,a=a):
#         self.a=12
# a=Test()
# print(a.b,a.c)


# class Test():
#     x=[1,2,3]
# a=Test()
# b=Test()
# a.x.append([1,2,3])
# print(a.x,b.x)
# c=list()
# d=list()
# c.append([1,2,3])



# class Test1():
#     def _init_(self):
#         self.x=[1,2,3]
# class Test2():
#     x=[1,2,3]
# a=Test1()
# b=Test1()
# a.x.append('abc')
# print('test01',a,=.x,b.x)
# c=Test2()
# d=Test2()
# a.x.append('abc')
# print('test02',a,=c.x,d.x)


# class parent():
#     def _init_(self):
#         self.p='我是父类'
#     def f(self):
#         print(self.p,'这是爸爸')
# class child(parent1,parent2,....):
#     def _init_(self):
#         self.c='我是子类'
#     def t(self):
#         print(self.c,'我要继承')
# a=child()
# a.t()
# a.f()


# class Test:
#     def _init_(self):
#         self._x=1
#         self.y=2

#     def _f(self):
#         print('这是密码')

# a=Test()
# print(a.y)

# a.f()
# a._f()

# class Test1():
#     def _init_(self):
#         self.t1='我是父类'

#     def f(self):
#         return'爸爸'

# class Test2():
#     def _init_(self):
#         self.t2='我是子类'

#     def f(self,abject):
#         print(abject.f())

# a=test1()
# b=Test2()
# b.f(a)
