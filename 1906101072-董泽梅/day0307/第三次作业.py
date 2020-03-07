#第一题
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名:{}'.format(self.name))
        print('年龄:{}'.format(self.age))
        print('性别:{}'.format(self.sex))
k=Person('Lucy',20,'女')
k.personInfo()

#第二题
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personIofo(self):
        print('姓名:{}'.format(self.name))
        print('年龄:{}'.format(self.age))
        print('性别:{}'.format(self.sex))
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        Person.__init__(self,name,age,sex)
        self.college=college
        self.professional=professional
    def personIofo(self):
        super().personIofo()
        print('学院:{}'.format(self.college))
        print('学系:{}'.format(self.professional))
    def teach0bj(self):
        print('今天讲了：面对对象设计程序')
m=Teacher('Nancy',30,'女','四川旅游学院','信息管理与信息系统')
m.personIofo()
m.teach0bj()


#第三题
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名:{}'.format(self.name))
        print('年龄:{}'.format(self.age))
        print('性别:{}'.format(self.sex))
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        Person.__init__(self,name,age,sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super.personInfo()
        print('学院:{}'.format(self.college))
        print('专业:{}'.format(self.professional))
    def teachObj(self):
        return'今天讲了：面向对象设计程序'
class Student(Person):
    def __init__(self,name,age,sex,college,banji):
        Person.__init__(self,name,age,sex)
        self.college=college
        self.banji=banji
    def personInfo(self):
        super().personInfo()
        print('学院:{}'.format(self.college))
        print('班级:{}'.format(self.banji))
    def study(self):
        print('老师%s,我终于学会了!'%Teacher.teachObj(self))
a=Student('Nancy',20,'女','信息与工程学院','19信管2班')
a.personInfo()
a.study()