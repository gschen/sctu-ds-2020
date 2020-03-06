#私有与公有
class Test:
    def __init__(self):
        self.__x=1 #私有变量，不能调用
        self.y=2 #公有变量

    def __f(self): #私有函数
        print('这是密码')

a=Test()
print(a.y)
print(a.__x)
a.f()
a.__f()
