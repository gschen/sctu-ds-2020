# 私有公有  在属性名前加两个下划线 __属性名
class Test:
    def __init__(self):
        self.__x=1
        self.y=2

    def __f(self):
        print('这是密码')
a=Test()
print(a.y)
print(a.x,a.__x) #无法调用