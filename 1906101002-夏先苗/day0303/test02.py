#构造方法
class Test():
    def __init__(self):
        print('已运行')
a=Test()

b=[1,2,3]
print(b)

class Test1():
    a=12
    def __init__(self,a=a):
        print(a)
a=Test1()
