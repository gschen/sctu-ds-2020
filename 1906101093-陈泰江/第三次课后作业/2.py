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
        print('今天讲了：面向对象设计程序')
Bob=Teacher('陈泰江',20,'男','信息与工程学院','信息管理与信息系统')
Bob.personinfo()
Bob.teachObj()