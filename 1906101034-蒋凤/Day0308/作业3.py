class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personlnfo(self):
        print('%s,%d,%s'%(self.name,self.age,self.gender))
        
class Teacher(object):
    def __init__(self,name,age,gender,college,professional):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.professional=professional
    def personlnfo(self):
        print('%s,%d,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序')

class Student(Person):
    def __init__(self,name,age,gender,collede,myclass):
        super(),__init__(name,age,gender)
        self.college=college
        self.myclass=myclass

    def personlnfo(self):
        super().personlnfo()
        print('我是%s的%s的学生'%(self.college,self.myclass))
    
    def study(self,tescher):
        print('我是%s,我终于学会了！'%(self.name,Teacher.teachObj()))

    def __str__(self):
        return '我是%s,年龄%s,性别%s,'%(self.name,self.age,self.gender)
    