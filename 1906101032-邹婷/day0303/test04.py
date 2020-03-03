#类变量
class Test():
    #实例变量
    def __init__(self):
        self.x=[1,2,3]
    #x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)

#类变量
class Test():
    x=[1,2,3]

#实例变量
    def __init__(self):
        self.x=[1,2,3]                            