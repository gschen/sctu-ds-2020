class Person():
    def __init__(self):
        self.name = "代恒"
        self.age = 18
        self.sex = "男"
    def personInfo(self):
        return self.name,self.age,self.sex
a=Person()
print(a.personInfo())
