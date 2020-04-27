#构造方法
# 
class Test():
    def _init_(self):
        self.x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)