#第三题
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
        return '今天讲了：面向对象设计程序'
class Student(Person):
    def __init__(self,name,age,sex,college,banji):
        Person.__init__(self,name,age,sex)
        self.college=college
        self.banji=banji
    def personInfo(self):
        super().personInfo()
        print(("college:%s,'banji:%s")%(self.college,self.banji))
    def study(self):
        print('老师%s，我终于学会了!'%Teacher.teachObj(self))
a=Student('zxy',19,'男','信息与工程学院','19信管3班')
a.personInfo()
a.study()
