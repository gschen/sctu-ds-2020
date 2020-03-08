class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(self.name,self.age,self.gender)
p=Person("邹婷","19岁","女")
print(p.personInfo())
