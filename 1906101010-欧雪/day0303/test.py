def res(ls):
    res=[0]*4
    for i in ls:
        if type(i)==int:
            res[1]=res[1]+1
        elif 65<=ord(i)<=90 and 97<=ord(i)<=122:
            res[0]=res[0]+1
        elif ord(i)==32:
            res[2]=res[2]+1
        else:
            res[3]+=1
    return res
print(res(["D",'a',' ','s',1,2,3,' ','a',2,'a','a']))
print(chr(97))

class MyClass:
    i=12345
def f(self):
    return 'hello world'
x=MyClass()
print("MyClass类的属性i为：",x.i)
print("MyClass类的方法f输出为：",x.f())

class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))

a=Test
a.original()
a.overturn()

class Test():
    b=12
    def__init__(self):
    self.a=12
a=Test()

print(a,b,a.c)

class Test():
    x[1,2,3]
a=test()
b=test()
a.x.append(['abc'])
print(a.x.b.x)

c=list()
d=list()
c.append([1,2,3])

class Test():
    def __inint__(self):
        self.x=[1,2,3]#类变量

class Test2():
    x=[1,2,3]
a=Test1()
b=Test1()
a.x.append('abc')
print('test01,a,x,b,x')

c=Test2()
d=Test2()
c.x.append('cde')
print('test01,c,x,d,x')

class Myclass():
    def __init__(self,a,b):#势力化时传入参数在这
        self.x=a
        self.y=b
        #self.xxx......
        #也可以写一些在实例化时便要执行的操作

    #定义函数往后
    def f1(self):
        #如果要调用实例变量
        c=self.x+self.y
        return c
    def __f2(self):
        pass

    
#类的继承

class parent():
    def __init__(self):
        self.p="我是父类"

    def f(self):
        print("财产1w")

class child(parent):
    def __init__(self):
        self.c="我是子类"
    def t(self):
        print(self.c,"我要继承")

a=child()
a.t()
a.f()

class parent():
    def __init__(self):
        self.p="我是父类"

    def f(self):
        print("财产1w")

class child(parent):
    def __init__(self):
        self.c="我是子类"
    def t(self):
        print(self.c,"我要继承")

a=child()
a.f()
super(child,a).f()

#私有公有

class Test():
    def __init__(self):
        self.__x=1
        self.y=2
    def __f(self):
        print("这是密码")
a=Test()
print(a.y)

a.f()
a.__f()


#类作参数

class Test1():
    def __init__(self):
        self.t1="我是父类"

    def f(self):
        return "爸爸"

class Test2():
    def __init__(self):
        self.t2="我是子类"

    def f(self,object):
        print(object.f())
a=Test1()
b=Test2()
b.f(a)