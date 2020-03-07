 """
 class Test():
   x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)

c=list()
d=list()
c.append([1,2,3])
"""


class parent():
    def__init__(self):
    self.p='我是父类'
def child():
    def__init__(self):
    self.c="我是子类"
    def t(self):
        print(self.c,"我要继承")

a=child()
a.t()
a.f()

class Test:
    def__init__(self):
    self.__x=1
    self.__y=2
    def__f(self):
       print(这是密码)
