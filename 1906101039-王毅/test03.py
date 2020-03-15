class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def personInfo(self):
        print("姓名：%s,年龄:%s,性别:%s" % (self.name,self.age,self.gender))
a=Person('王毅',18,'男')
a.personInfo()

 class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('姓名:%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender)) 
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('我是来自%s%s的一名讲师'%(self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象设计程序'

teacher=Teacher('王毅',18,'男','四川旅游学院','信息与工程学院')                                                                          
teacher.personInfo()
teacher.teachObj

class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print('姓名',self.name)
        print('年龄',self.age)
        print('性别',self.sex)
class Teacher(Person):
    def __init__(self,name,age,sex,collage,professional):
        Person.__init__(self,name,age,sex)
        self.collage=collage
        self.professional=professional
    def personinfo(self):
        super().personinfo()
        print('学院',self.collage)
        print('专业',self.professional)
    def teachObj(self):
        return '今天讲了：面向对象设计程序'
class Student(Person):
    def __init__(self,name,age,sex,collage,banji):
        Person.__init__(self,name,age,sex)
        self.collage=collage
        self.banji=banji
    def personinfo(self):
        super().personinfo()
        print('学院',self.collage)
        print('班级',self.banji)
    def study(self):
        print('老师%s，我终于学会了!'%Teacher.teachObj(self))
a=Student('王毅',18,'男','信息与工程学院','19信管1班')
a.personinfo()
a.study()

