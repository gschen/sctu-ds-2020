class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
    def personlnfo(self):
        print('姓名：%s,年龄：%s,性别：%s,学院：%s,专业：%s'%(self.name,self.age,self.sex,self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象程序设计'
class Student(Person):
    def __init__(self,name,age,sex,college,banji):
        super().__init__(name,age,sex)
        self.college=college
        self.banji=banji
    def personlnfo(self):
        print('姓名：%s,年龄：%s,性别：%s,学院：%s,班级：%s'%(self.name,self.age,self.sex,self.college,self.banji))
    def study(self,Teacher):
        print('老师%s，我终于学会了'%(Teacher.teachObj(self)))
a=Student('李诗尧',18,'女','信息与工程学院','3班')
a.personlnfo()
a.study(Teacher)