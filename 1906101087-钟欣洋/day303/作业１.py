#第一题
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
     print(("name:%s,age:%s,sex:%s") % (self.name,self.age,self.sex))

A=Person("liumin",19,"女")
A.personInfo()
