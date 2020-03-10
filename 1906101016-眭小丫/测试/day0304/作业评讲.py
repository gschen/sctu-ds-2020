class Person():
    def _init_(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def personInfo(self):
        print(self.name,self.age,self.sex)

xiaom=Person('王小明',24,'男')
xiaom.personInfo()

class Teacher(Person):
    def _init_(self,name,age,sex,college,professional):
        self.name=name
        self.age=age
        self.sex=sex 
        self.college=college
        self.professional=professional

    def personInfo(self):
        print(self.name,self.age,self.sex,self.college,self.professional)

    def teachobj(self):
        return '今天讲了：面向对象设计'

laoshi=Teacher('王老师',32,'男','信工学院','信息管理与信息系统')
laoshi.personInfo()


class Student(Person):
    def _init_(self,name,age,sex,college,classmub):
        super()._init_(name,age,sex)
        self.college=college
        self.classmub=classmub

    def personInfo(self):
        print(self.name,self.age,self.sex,self.college,self.classmub)

    def study(self,object):
        recept=object.teachobj()
        print('老师{},我终于学会了！'.format(recept))

xm=Student('小明',25,'男','信工学院',3)
xm.study(laoshi)