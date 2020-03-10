#类代码
class Myclass():
    i=123456
    def f(self,ostr):
        print(ostr)
x=Myclass()
print(x.i,x.f('hello world'))


class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()

