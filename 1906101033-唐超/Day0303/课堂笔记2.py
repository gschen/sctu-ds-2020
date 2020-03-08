#类
class MyClass:
    i=123456
    def f(self,ostr):
        print(ostr)

x=MyClass()
print(x.i,x.f('hello,world'))




class Test():
    def original(seif):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()



#类变量在整个实例化的对象中是公用的

class Test1():
    def __init__(self):   
        self.x=[1,2,3] #实例变量
 


class Test2()：
    x=[1,2,3]#类变量

#Test01
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

#test02
c=Test2()
d=Test2()
c.x.append('abc')
print('test02',c.x,d.x)



#类的继承
class parent():
    def __init__(self):
        self.p='我是父亲'

    def f(self):
        print('财产1w')

class child(parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')   

a=child()
a.t()
a.f()

# 注意点:
# 1.当子类方法与父类方法重名，优先
# 调用子类中的方法。
# 2.在继承多个父类时，调用父类方法
# 会从左至右依次检索每个父类中是否有该
# 方法。

#覆盖调用,方法重写。
#当子类方法与父类方法重名，需要越过子类，调用父类方法重写:继承的父类方法不能满
#足需求，在子类中直接重写该方法

#私有公有  没办法调用私有属性和私有方法
class Test:
    def __init_ (self):
        self.__x=1
        self.y=2
    def __f(self):
        print( '这是密码')

a=Test( )
print(a.y)

a.f()
a.__f()


#类作参数  对象作为参数传递
class Test():
    def __init__(self):
        self.t1='我是父亲'
    def f(self):
        return '爸爸'

class Test2()：
    def __init__(self):
        self.t2='我是子类'

    def f(self,object):
        print(object.f())

a=Test1()
b=Test2()

def main(object):
    print(object.f())
    return 
