class MyClass():#()不加也可运行
    i=123456
    def f(self,ostr):#self一定要写
        print(ostr)

x=MyClass()无论第一行是否写（），此处都要写（）
print(x.i,x.f('hello,word'))


class Test():#类名大写
    def original(self):
        lis = [chr(i) for i in range(91, 123)]
        print(''.join(lis))

    def overturn(self):
        print(''.join([chr(i) for i in range(90, 64, -1)]))

a = test()
a.original()
a.overturn()

#构造方法 __init__
Class Test():
    def __init__(self):
        print('已运行')
a=Test()#类不可以传参

Class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)

Class Test():
    a=12
    def __init__(self,a=a):
        print(a)
a=Test()

Class Test():
    b=12
    def __init__(self):
        self.c=12#定义实列变量
a=Test()
print(a,b,c)

b=list([1,2,3])
print(b)

Class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])#类变量在实列化中都是公用的
print(a.x,b.x)#b也会受影响

#实列变量与类变量的区别：类变量在整个实列化对象中都是公用的；实列变量属于实列化的现象；   一般使用实列变量
Class Test1():
    def __init__(self):
        self.x=[1,2,3]#实列变量,b不受影响
#test01
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

#test02
c=Test2()
d=Test2()
a.x.append('cde')
print('test02',c.x,d.x)

#类的标准写法
Class MyClass():
    def __init__(self,a,b):#实列化时传入参数在这
        #定义变量在此处！！！
        self.x=a
        self.y=b
        #self.xxx....
        #也可以写一些在实列化时便于执行的操作
    #定义函数往后
    def f1(self):
        #如果要调用实列变量-----self.变量名
        c=self.x+self.y
        return c
    def f2(self):
        pass
