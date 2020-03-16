


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



class Student(Person):
    def __init__(self,name,age,sex,college,class1):
        self.name=name
        self.age=age
        self.sex=sex
        self.collage=college
        self.class1=class1
    def personInfo(self):
        print('我叫%s,年龄%s，性别%s，学院%s，班级%s'%(self.name,self.age,self.sex,self.collage,self.class1))
    def study(self,object):
        print('老师%s,我终于学会了！'%object.teachObj())

a=Student('糖糖','18岁','女','信息与工程学院','信管03')
a.personInfo()
b=Teacher()
a.study(b)

