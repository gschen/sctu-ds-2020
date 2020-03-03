[1.2.3.4]
for a in range(1,5):
    for b in range(1,5):
        for i in range(1,5):
            if a != b and b!=i and a!= i:
                print('{}{}{}'.format(a,b,i))

x,y,z=map(int,input().spilt())
l=[x,y,z]
l.sort()
print(l)

def r(n):
    sums=0
    if n%2==0:
        for i in range(2,n+1,2):
            sums=sums+(1/i)
            return sums
    else:
        for i in range(1,n+1,2):
            sums=sume+(1/i)
            return sums
print(r(6))

def re(ls):
    re=[0]*4
    for i in ls:
        if 65<=ord(i)<=90 and 97<=ord(i)<=122:
            re[0]=re[0]+1
        elif 48<=ord(i)<=57:
            re[1]=re[1]+1
        elif ord(i)==32:
            re[2]=re[2]+1
        else:
            re[3]+=1
    return re
print(re(['D','a','','s',1,3,2]))

class myclass:
    i=123456
    def f(self,ostr):
        print(ostr)
x=myclass()
print(x.i,x.f('helloword'))

class Test:
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))

a=Test()
a.original()
a.overturn()

class Test:
    b=12
    def __int__(self):
        self.c=12
a=Test()

print(a.b,a.c)

class Test1():
    def __int__(self):
        self.x=[1,2,3]#实例变量

class Test2():
    x=[1,2,3]#类变量
#test01    
a=Test1()
b=Test1()
a.x.append('abc')
print('test01',a.x,b.x)

#test02
c=Test2()
d=Test2()
c.x.append('cde')
print('test02',c.x,d.x)

class parent():
    def __int__(self):
        self.p='我是父类'
    def f(self):
        print(self.p,'财产1w')
class child(parent):
    def __int__(self):
        self.c='我是子类'
    def t(self):
        print(self.c,'我要继承')

a=child()
a.t()
a.f()

class Test:
    def __int__(self):
        self.__x=1#私有变量
        self.y=2
    def __f(self):#私有方法
        print('这是密码')


a=Test()
print(a.y)

a.f()
a.__f()


