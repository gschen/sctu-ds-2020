class MyClass():
    i=123456
    def f(self,ostr):#self一定要写
        print(ostr)

x=MyClass()#不管第一行写不写()，此处都要写()
print(x.i,x.f('hello,world'))

