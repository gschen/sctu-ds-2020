#类
if type('1')==int:
    print('yes')



class MyClass:
    i=12345
    def f(self,ostr):
        print(ostr)
x=MyClass()
print(x.i,x.f('hello,world'))

class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
      def overturn(self):
          print(''.join([chr(i) for i in range(65,91)]))
#构造  
a=Test()
a.original()
a.overurn()

class Test():
    def __init__(self,a,b):
        self.a=12
        print('一运行',a+b)
a=Test(10,20)

#类变量
class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.xappend(['abc'])
print(a.x,b.x)

class Test():
    x=1
a=Test()
a.x=2
b=Test()
print(a.x,b.x)

#实例变量
class Test():
    def __init__(self):
        self.x=[1,2,3]
a=test()
b=test()
a.x.append(['abc'])
print(a.x,b.x)



#实例变量
class Test1():
    def __init__(self):
        self.x=[1,2,3]
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

#类变量
class Test2():
    x=[1,2,3]
c=Test2()
d=Test2()
c.x.append('cde')
print('test02',c.x,d.x)


#类的标准写法
class Myclass():
    def __init__(self,a,b):#实例化时传入参数在这
        #定义变量在此处
        self.x=a
        self.y=b
        #也可以写一些在实例化时便要执行的操作

    #定义函数后
    def f1(self):
        #如果要调用变量。。》self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass
    
    

#类的继承
class parent():
    def __init__(self):
         self.p='我是父类'
    def f(self):
        print('财产')

class child(parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')
a=child()
a.t()
a.f()
super(child,a).f()

#私有变量
class Test:
    def __init__(self):
        self.__x=1
        self.y=2

    def __f(self):
        print('密码')

a=Test()
print(a.y)
print(a.x,a.__x)
a.f()
a.__f()

#类作为参数
class Test1():
    def __init__(self):
        self.t1='我是父类'

    def f(self):
        retuen '爸爸'

class Test2():
    def __init__(self):
        self.t2='我是子类'

    def f(self,object):
        print(object.f)

a=Test1()
    b=Test2()
b.f(a)

def main(object):
    print(object.f())
    return '1213'
print(main())
