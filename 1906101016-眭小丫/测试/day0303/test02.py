class Test():
    def original(self):
        list1=[chr(i) for i in range(97,123)]
        print(''.join(list1))
    def overturn(self):
        print(''.join([chr(i) for i in range(98,64,1)]))
a=Test()
a.original()
a.overturn()