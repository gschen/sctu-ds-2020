class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
            print(a.name,a.age,a.gender)
a=Person("小明","17","女")
a.personInfo()