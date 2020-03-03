class Myclass:
    i=12345
    def f(self,ostr):
        print(ostr)

x=MyClass()
print(x,i,x,f('hello,word'))

class Test():
    def original(self):
        lis=[chi(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chi(i) for i in range(90,64,-1)]))

a=Test()
a.original()
a.overturn()

class Test():
    def __init__(self,a,b):
        print('已运行',a+b)
a=Test(10,20)
