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