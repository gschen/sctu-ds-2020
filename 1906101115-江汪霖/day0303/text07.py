class Test():
    def __init__(self):
        self.__x=1  #__隐藏的变量不可调用
        self.y=2

    def f(self):
        print("这是密码")

a=Test()
print(a.y)
print(a.__x,a.__x)
a.f()
