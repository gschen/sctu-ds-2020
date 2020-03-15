class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('姓名:%s,年龄:%s,性别:%s'%(self.name,self.age,self.gender))
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        self.anme=name
        self.age=age
        self.gender=gender
        self.college=college
        self.professional=professional
    def personInfo(self):
        print('学院:%s,专业:%s'%(self.college,self.professional))
    def teachObj(self):
        return('今天讲了:面向对象程序设计')

a=Teacher('Bob',18,'男','信息与工程学院','信息管理与信息系统')
a.personInfo()