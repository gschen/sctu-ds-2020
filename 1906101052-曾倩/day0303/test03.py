class Test():
    def __init__(self):
        self.x=[1,2,3]
class Test2():
    x=[1,2,3]

#test1
a=Test()
h=Test()
a.x.append('abc')
print('test1',a.x,b.x)

#test2
c=Test2()
d=Test2()
c.x.append('cde')
print('test2',c.x,d.x)
