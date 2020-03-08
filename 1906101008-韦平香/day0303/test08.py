class Test:
    def __init__(self):
        self.__x=1
        self.y=2

    def __f(self):
        print('我是密码')

a=Test()
print(a.y)
print(a.__x)
a.f()
a.__f