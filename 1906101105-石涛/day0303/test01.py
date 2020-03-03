# coding=utf-8

'---------------------------------------------------'
''' python类 '''
# 类：是代码和函数的封装体

# calss 类名：
#     代码块/函数

#类变量和实列变量统称为属性

# 打印hello world
class Myclass:
    i=123456
    def f(self,ostr):
        print(ostr)

x=Myclass()
print(x.i,x.f('hello world !'))

# 打印字母
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))

a=Test()
a.original()
a.overturn()


'-----------------------------------------------------------------'
'''构造方法'''
# (类的内置函数，这里用__init__)

'''1'''
class Test1():
    c=12 # 类里面的变量也为局部变量
    def __init__(self,a,b):
        print('已运行')
        print(a+b)

a=Test1(10,20)


#类变量和实例变量的区别
'''类变量'''
class Test2():
    x=[1,2,3]

a=Test2()
b=Test2()
a.x.append([1,2,3])
print(a.x,b.x)
# 类变量在整个实例化变量中是通用的

'''实例变量'''
class Test3():
    def __init__(self):
        self.x=[1,2,3]

c=Test3()
d=Test3()
c.x.append(['abc'])
print(c.x,d.x)
# 实例变量属于实例化的对象

# 类的标准写法
class Myclass1():
    def __init__(self,a,b): # 实例化时传入参数在这儿
        #定义变量在此处
        self.x=a
        self.y=b
        #也可以写一些实例化时便要执行的操作

    # 定义函数往后
    def f1(self):
        # 这里可以写函数，变量可以用之前的变量
        c=self.x
        print(c)

'---------------------------------------------------------------------'
'''面向对象'''
# 面向过程是自己需要些底层的代码，面向对象就是我们直接用别人已经编好的代码
# 面向对象就是使用类

'---------------------------------------------------------------------'
'''类的继承'''
# 一个类通过继承获取另外一个类的方法
# class 类名（继承的类）：
#     <statement-1>
#     ......
#     ......

class father():
    def __init__(self):
        self.p='我是父类'
    
    def f(self):
        print('我是父类，财产1w亿')

class child(father):
    def __init__(self):
        self.c='我是子类'
    
    def t(self):
        print(self.c,'我要继承')

a=child()
a.f()
a.t()
# 注意：就是父子类里的函数名重复，则优先调用子类的

'------------------------------------------------------'
'''共有私有'''

# 当类中的某些方法不需要被使用者调用，可以将这些属性或方法私有化
# 私有化方法：__属性名/函数名

'--------------------------------------------------------'
'''类作为参数传入'''

class Test4():
    def __init__(self):
        self.t1='我是父类'

    def f(self):
        return '爸爸'

class Test5():
    def __init__(self):
        self.t2='我是子类'

    def f(self,object):
        print(object.f())

a=Test4()
b=Test5()
b.f(a)

def main(object):
    print(object.f())

    return '123'

print(main(a))