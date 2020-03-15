#类 
'''class Myclass():
    i = 123456
    def f(self,oster):
        print(oster)
        
x = Myclass()
print(x.i,x.f("hello, cc"))'''

class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()
'''
class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a = Test(10,20)'''
'''
class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)#b受到影响 类变量共用'''
'''
class Parent():
    def __init__(self):
        self.p='我是父类'
        
    def f(self):
        print(self.p,'财产1w')
        
class child(Parent):
    def __init__(self):
        self.c='我是子类'
    def f(self):
        print(self.c,'我要继承')
a=child()
a.f()
#super(child,a).f()'''





