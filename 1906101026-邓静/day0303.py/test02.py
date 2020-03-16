class Test():
    def original(self):
        lis=[chr(i) for i in range(97,123)]
        print(lis)
    def overturn(self):
        print([chr(i) for i in range(90,64,-1)])

a=Test()
a.original()
a.overturn()
