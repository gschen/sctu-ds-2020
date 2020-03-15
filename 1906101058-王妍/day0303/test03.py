#第三题
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class Teacher(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
    def PersonIofo(self):
         print("姓名：%s,年龄：%s,性别:%s,学院:%s,专业:%s" % (self.name,self.age,self.sex,self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象程序设计'
class Student(Person):
    def __init__(self,name,age,sex,college,classroom):
        super().__init__(name,age,sex)
        self.college=college
        self.classroom=classroom
    def personIofo(self):
        print("姓名：%s,年龄：%s,性别:%s,学院:%s,班级:%s" % (self.name,self.age,self.sex,self.college,self.classroom))
    def study(self,Teacher):
        print('老师%s,我终于会了！' %(Teacher.teachObj(self)))
a=Student('王妍',18,'女','信管','2班')
a.personIofo()
a.study(Teacher)
