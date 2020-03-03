class Test():
    def __init__(self):
        self.__x=1
        self.y=2

    def __f(self):
        print("这是密码")
a=Test()
print(a.y)
print(a.x,a.__y)
a.f()
a.__f()

#私有，无法查看