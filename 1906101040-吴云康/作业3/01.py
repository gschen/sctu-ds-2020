class Person():
    def __init__(self):
        self.name = "吴云康"
        self.age = 20
        self.gender = "male"
    def personInfo(self):
        return self.name,self.age,self.gender
x = Person()
print(x.personInfo())