class Test1():
    def __init__(self):
        self.x=[1,2,3]

class Test():
    x=[1,2,3]

a=Test()
b=Test()
a.x.append(['abc'])
print(a.x,b.x)

c=Test1()
d=Test1()
c.x.append('ade')
print(c.x,d.x)