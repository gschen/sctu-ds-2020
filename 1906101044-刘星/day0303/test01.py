class MyClass:
    i=123456
    def f(self,ostr):
        print(ostr)
x=MyClass()
print(x.i,x.f('hello,word'))



class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()


class Test():
    def __init__(self):
        print('已运行')
a=Test()
b=list([1,2,3])
print(b)


class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

class Test2():
    x=[1,2,3]#类变量
c=Test2()
d=Test2()
c.x.append('def')
print('test02',c.x,d.x)


class parent():
    def __init__(self):
        self.p='我是父类'
    def f(self):
        print('财产1w')
class child(parent):
    def __init__(self):
        self.c='我是子类'
    def f(self):
        print(self.c,'我要继承')
a=child()
a.f()
super(child,a).f()


class Test:
    def __init__(self):
        self.__x=1
        self.y=2
    def __f(self):
        print('这是密码')
a=Test()
print(a.y)


class Test1():
    def __init__(self):
        self.t1='我是父亲'
    def f(self):
        return '爸爸'
class Test2():
    def __init__(self):
        self.t2='我是子类'
    def f(self,object):
        print(object.f())
a=Test1()

def main(object):
        print(object.f())
        return '123'
print(main(a))