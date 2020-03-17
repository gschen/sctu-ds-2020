#1
class Myclass:
    i=123456
    def f(self,ostr):
        print(ostr)

x=Myclass()
print(x,i,x,f('hello,world'))

#2
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
    def overturn(self):
        print('',join([chr(i) for i in range(0,64,-1)]))

a=Test()
a.original()
a.overturn()

class Test1():
    def __init__(self):
        self.x=[1,2,3] #实例变量


class Test2():
    x=[1,2,3] #类变量
#test01
a=Test1()
b=Test2()
a.x.append('abc')
print('test01',a.x,b.x)

#test02
c=Test2()
d=Test2()
c.x.append('cde')
print('test02',c.x,d.x)


#test6


#test7
class parent():
    def __init__(self):
        self.p='我是父类'

    def f(self):
        print(self.p,'财产1w')

class child(parent):
    def __init__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.t()
a.f()


#test8
class Test:
    def __init__(self):
        self.__x=1
        self.y=2

    def __f(self):
        print('这是密码')

a=Test()
print(a.y)

a.f()
a.__f()


#test9

