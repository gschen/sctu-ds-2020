class MyClass(): #不加“()”也能运行
    i=123456
    def f(self,ostr):
        print(ostr)
x=MyClass()
print(x.i,x.f('hello,word'))