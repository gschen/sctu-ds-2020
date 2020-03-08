class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
         print(("name:%s,age:%s,sex:%s")%(self.name, self.age,self.sex))
yi=Person("张三",20,"男")
yi.personInfo()


#2    
class Person(object):
    def _init_(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print(("name:%s,age:%s,sex:%s")%(self.name,self.age,self.sex))
class Teacher(Person):
    def __init__(self,name,age, sex,collage,professional):
        Person. __init__ (self,name,age,sex)
        self.collage=collage
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('college',self.collage)
        print('professional',self.professional)
    def teach0bj(self):
        print('今天讲了： 面向对象设计程序')
yi=Teacher('李四',20,'男','信息与工程学院','信息管理与信息系统')
yi.personInfo()
yi.teach0bj()


#3
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
        person.__init__(self,name,age,sex)
        self.collage=collage
        self.professional=professional
    def personinfo(self):
        super().personinfo()
        print('学院',self.collage)
        print('专业',self.professional)
    def teach0bj(self):
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
        print('老师%s,我终于学会了!'%Teacher.teach0bj(self))
a=Student('汤姆',20,'男','信息与工程学院','19信管2班')
a.personinfo()
a.study()

   

