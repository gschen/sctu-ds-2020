class MyClass:
    i = 12345
    def f(self,ostr):
        return ostr


x = MyClass()
print(x.i,x.f("hello,world"))