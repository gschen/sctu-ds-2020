#python-类（class）
'''
class 类名:
    代码块/函数
'''
'''
class Myclass():
    i=12345
    def f(self,mjj):
        print(mjj)

x=myclass()
print(x.i,x.f('hello world'))   
'''
'''
class Test():
    def original(self):
        list=[chr(i) for i in range(97,123)]
        print(''.join(list))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))    
a=Test()
a.original() 
a.overturn()  
'''
'''
class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)        
'''
'''
class Test():
    def __init__(self):
        self.x=[1,2,3]#实例变量
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)

c=list()
d=list()
c.append([1,2,3])
'''
'''
class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量

class Test2():
    x=[1,2,3]#类变量

#test01
a=Test1() 
b=Test1() 
a.x.append('abc')
print('test01',a.x,b.x)

#test02
a=Test2() 
b=Test2() 
a.x.append('cde')
print('test02',a.x,b.x)
'''
#类的标准写法
'''
classMyclass():
    def __init__(self,a,b):#实例化时传入参数在这
    #定义变量在此处
        self.x=a
        self.x=b
    #self.xxx.....
    #也可以写一些在实例化时便要执行

    #定义函数后
    def f1(self):
        #如果要调用实例变量-->self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass    
'''
#类的继承
'''
class parent():
    def __init__(self):
        self.p='我是父类'
    def f(self):
        print('财产1w')

class child(parent):
    def __init__(self):
        self.q='我是子类'
    def t(self):
        print(self.q,'我要继承')

a=child()
a.t()
a.f()
'''
#私有公有
'''
class test:
    def __init__(self):
        self.__x=1
        self.y=2
    def __f(self):
        print('这是密码')    

a=test()
print(a.y)
print(a.x,a.__x)
a.f()
a.__f()
'''
'''
#class Test01():
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
#print(main(a))
'''