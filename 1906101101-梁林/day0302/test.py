# 练习
# class mj():
#     i = 456151
#     def f(self,j):                        
#         return j
# a = mj()
# print(a.i)
# print(a.f(5))

# #练习
# class Test():
#     def original(self):
#         return ''.join(list(map(chr,list(range(97,123)))))
#     def overturn(self):
#         return ''.join(list(map(chr,list(range(65,91))))[::-1])
# a=Test()
# print(a.original())
# print(a.overturn())

# #练习
# class Test1():
#     def __init__(self):
#         print('dfg')
# a=Test1()

# class Test2():
#     def __init__(self,k):
#         print('dfg',k)
# a=Test2(5)

# 类变量公用
# class Test():
#     x=[1,2,3]

# a=Test()
# b=Test()
# a.x.append('abc')
# print(a.x,b.x)

# #实例变量
# class Test():
#     def __init__(self):
#         self.x=[1,2,3]
# a=Test()
# b=Test()
# a.x.append('abc')
# print(a.x,b.x)

# #继承
# class f():
#     def __init__(self):
#         self.x='123'
#     def k(self):
#         print('abc')
# class e(f):
#     def __init__(self):
#         self.y='456'
#     def k(self):#重名时先调用子类
#         print(self.y,'sdfsdfsd')
# a=e()

# a.k()
# super(e,a).k()#调用父类同名

# #私有变量
# class Test():
     
#     def __init__(self):
#         self._x=1
#         self.y=2        
#     def _f(self):
#         print('541616')
# a=Test()
# print(a.x)

# a.f()
# a._f()

#对象做参数传入
class Test1():    
    def __init__(self):
        self.x=4      
    def f(self):
        print('541616')
class Test2():
    def __init__(self):
        self.x=4       
    def k(self,object):
        print(object.f())
a=Test1()
b=Test2()
b.k(a)

