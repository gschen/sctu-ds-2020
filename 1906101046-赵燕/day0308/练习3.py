class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def PersonInfo(self):
        print('我的姓名:%s,年龄:%s,性别:%s'%(self.name,self,age,self.gender))
class Teacher(Person):
    def __init__(self,name,age,gender,college,porfessional):
        super().__init__(name,age,gender)
        self.college=college
        self.porfessional=porfessional
    def PersonInfo(self):
        print('老师叫做%s,年龄:%s,性别：%s,他在%s学院，教%s'%(self.name,self.age,self.gender,self.college,self.porfessional))
    def TeachObj(self):
        return '今天讲了面向对象'
class Student(Person):
    def __init__(self,name,age,gender,college,grade):
        super().__init__(name,age,gender)
        self.college=college
        self.grade=grade
    def PersonInfo(self):
        print('我的名字:%s,今年%s岁，是个%s生，在%s,学的%s'%(self.name,self.age,self.gender,self.college,self.grade))
    def Student(self,teacher):
        print('老师%s我终于学会了!'%(teacher.TeachObj(self)))
z=Student('赵燕',19,'女','信息与工程学院','信息')
z.PersonInfo()
z.Student(Teacher)

