class Test():
    list_ot=[]
    x=1
    def __init__(self):
        self.lis_in=[]





class MyClass:
    i=123456
    def f(self,ostr):
        print(ostr)
x=MyClass()
print(x.i,x.f("hello,world"))


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
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)
c=list()
d=list()
c.append([1,2,3])







class Test():
    b=12
    def __init__(self):
        self.c=12
a=Test()
print(a.b,a.c)

#l类变量
class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)
#实例变量
class Test():
    def __init__(self):
        self.x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)



#类的标准写法
class MyClass():
    def __init__(self,a,b):#实例化时传入参数在这
        #定义变量在此处
        self.x=a
        self.y=b
        #self.xxx……
        #也可以写一些在实例化时便要执行的操作


class parent():
    def __init__(self):
        self.p="我是父类"
    def f(self):
        print("财产1w")
class child(parent1,parent2,……):
    def __init__(self):
        self.c="我是子类"
    def t(self):
        print(self.c,"我要继承")
a=child()
a.t()
a.f()


class Test():
    def __init__(self):
        self.__x=1
        self.y=2
a=Test
print(a.y)
print(a.__x)
a,f()
a.__f()





class Test1():
    def __init__(self):
        self.t1='我是父类'
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