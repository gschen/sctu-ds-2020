class Myclass:
    i=12345
    def f(self,ostr):
        print(ostr)

x=Myclass()
print(x.i,x.f('hello,world'))