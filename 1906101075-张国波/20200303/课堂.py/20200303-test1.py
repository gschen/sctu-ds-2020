class MyClass:
    i=12345
    def f(self,ostr):
        print(ostr)

x=MyClass()
print(x.i,x.f('hello word'))