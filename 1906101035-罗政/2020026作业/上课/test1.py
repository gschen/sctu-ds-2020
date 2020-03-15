class Test():
    def original(self):
        list=[chr(i) for i in range(97,123)]
        print("".join(list))
    def overturn(self):
        print("".join([chr(i) for i in range(90,64,-1)]))


a=Test()
a.original()
a.overturn()