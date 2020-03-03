#1.
class Test(): #类名要大写
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
a=Test()
a.original()

#2.
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
    def overturn(self):
        print('',join([chr(i) for i in range(65,91)]))
a=Test()
a.original()

#3.
class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print('',join(lis))
    def overturn(self):
        print('',join([chr(i) for i in range(90,64,-1)]))
a=Test()
a.original()
a.overturn()