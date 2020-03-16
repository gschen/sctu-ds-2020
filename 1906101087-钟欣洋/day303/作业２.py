#第二题
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print(("name:%s,age:%s,sex:%s")%(self.name,self.age,self.sex))

class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        Person.__init__(self,name,age,sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print(("college:%s,professional:%s")%(self.college,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序')

Ｂ=Teacher('xiaoming',27,'男','信息与工程学院','信息管理与信息系统')
Ｂ.personInfo()
Ｂ.teachObj()