class Test:
    def __int__(self):
        self.__x=1#私有变量
        self.y=2
    def __f(self):#私有方法
        print('这是密码')


a=Test()
print(a.y)

a.f()
a.__f()