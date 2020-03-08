class Test():
    def __init__(self):
        print('已运行')
a=Test()

b=list([1,2,3])
print(b)

class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)