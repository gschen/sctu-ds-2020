#构造方法
class Test():
    b=12
    def __init__(self):
        self.c=12
a=Test()
print(a.b,a.c)

class Test():
   def __init__(self,a,b):
       print('已运行',a+b)
a=Test(10,20)