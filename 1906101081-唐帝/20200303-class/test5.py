class Test():
    def __init__(self):
        self.x=[1,2,3]
    x=[1,2,3]
a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)