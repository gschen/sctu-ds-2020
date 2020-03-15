class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print("".join(lis))
    def overturn(self):
        print("".join([chr(i) for i in range(90,64,-1)]))

a=test()
a.original()
a.oyerturn()



#
Class Test():
    x=[1,2,3]
a=Test()
b=Test()
a.x.append([1,2,3])
print(a.x,b.x)


c=list()
d=list()
c.append([1,2,3])