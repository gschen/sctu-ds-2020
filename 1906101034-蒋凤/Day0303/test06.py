class Test():
    def __init__(self):
        self.x=[1,2,3]

a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)

c=list()
d=list()
c.append([1,2,3])