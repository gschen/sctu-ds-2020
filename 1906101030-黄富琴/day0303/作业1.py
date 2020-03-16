class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def personInfo(self):
        print(self.name,self.age,self.gender)

a=Person('Bob',18,'男')
a.personInfo()