


class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    
    def personInfo(self):
        print(self.name,self.age,self.sex)


class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        self.name=name
        self.age=age
        self.sex=sex
        self.collage=college
        self.professional=professional
    def personInfo(self):
        print(self.name,self.age,self.sex,self.collage,self.professional)
    def teachObj(self):
      print('今天讲了：面向对象设计程序')
    
a=Teacher('糖糖','18岁','女','信息与工程学院','信息管理与信息系统专业')
a.personInfo()
a.teachObj()
