class Test():
    def one(self):
        lis=[chr(i) for i in range (97,123)]
        print(''.join(lis))
    def two(self):
        print(''.join([chr(i) for i in range (65,91)]))
a = Test()
a.one()
a.two()