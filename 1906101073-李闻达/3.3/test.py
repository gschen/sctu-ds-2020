class Test():
    def one(self):
        lis=[chr(i) for i in range (97,123)]
        print(''.join(lis))
    def two(self):
        print(''.join([chr(i) for i in range (65,91)]))
a = Test()
a.one()
a.two()



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



class Test1():
    def __init__(self):
        self.t1='我是父亲'
    def f(self):
        return "爸爸"

class Test2():
    def __init__(self):
        self.t2='我是子类'

    def f(self,object):
        print(object.f())
a=Test1()

def main(object):
    print(object.f())
    return '123'

print(main(a))    