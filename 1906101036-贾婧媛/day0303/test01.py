class MyClacc():#()不加也能运行
    i=123456
    def f(self,ostr):#self一定要写
        print(ostr)

x=MyClass()#不管第一行写不写(),此处都要写()
print(x,i,x.f('hello,word'))



class Test():#类名大写
    def original(self):
        lis= [chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))

a = Test()
a.original()
a.overturn()


#构造方法 __init__()
class Test():
    def __init__(self):
        print('已运行')
a=Test()#类不可以传参


class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)

class Test():
    a=12
    def __init__(self,a=a):
        print(a)
a=Test()

class Test():
    b=12
    def __init__(self):
        self.c=12#定义实例变量
a=Test()
print(a,b,c)

b=list([1,2,3])
print(b)

class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)

class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])#类变量在实例化中都是公用的
print(a.x,b.x)     #b也会受到影响


class Test():
    def __init__(self):
        self.x=[1,2,3]#实例变量，b不受影响
     
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)

#实例变量与类变量的区别：
#类变量：类变量在整个实例化对象中是公用的
#实例变量：属于实例化的对象
#一般使用类变量，实例变量易出错
class Test1():
    def __init__(self):
        self.x=[1,2,3]#实例变量
#test01
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

class Test():
    x=[1,2,3]#类变量
#test02
a=Test2()
b=Test2()
a.x.append('cde')
print('test02',c.x,d.x)

#类变量的标准写法
class MyClass():
    def __init__(self,a,b):#实例化时传入参数在这
        #定义变量在此处
        self.x=a
        seif.y=b
        #self.xxx.........
        #也可以写一些在实例化时便于执行的操作
    
    #定义函数往后
    def f1(self):
        #如果要调用实例变量--> self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass
    
    
    #......