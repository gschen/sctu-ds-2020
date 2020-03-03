class Test():
    def original(self):
        lis=[chr(j) for j in range(97,123)]
        print(''.join(lis))
    def overturn(self):
        print(''.join([chr(j) for j in range(90,64,-1)]))

a=Test()
a.original()
a.overturn()