#创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def PersonInfo(self):
        print('姓名:%s,年龄:%s,性别:%s'%(self.name,self.age,self.sex))
a=Person('邓静',19,'女')
a.PersonInfo()

class Teacher(object):
    def __init__(self,name,age,gender,college,professional):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.professional=professional
    def personInfo(self):
        print('%s,%d,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序')
a=Teacher('邓静',19,'女','四川旅游学院','信息管理与信息系统')
a.personInfo()
a.teachObj()

class Student(Person):
    def __init__(self,name,age,gender,college,myclass):
        super().__init__(name,age,gender)
        self.college=college
        self.myclass=myclass
    def PersonInfo(self):
        super().PersonInfo()
        print('我是%s的学生'%(self.college,self.myclass))
    def study(self,teachObj):
        print('我是%s,我终于学会了!'%(self.name,Teacher.teachObj()))
    def __str__(self):
        return '我是%s,年龄%s,性别%s'%(self.name,self.age,self.gender)
a=Student('dj',19,'nv','g','1')
a.PersonInfo()
a.study()

