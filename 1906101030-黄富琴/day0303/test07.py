class Test():
    def __init__(self):
        self.__x=1
        self.y=2
    
    def __f(self):
        print('hello')

a=Test()
print(a.y)

a.f()
a.__f()