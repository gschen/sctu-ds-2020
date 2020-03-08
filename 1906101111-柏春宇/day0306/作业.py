class Person(object):
    def __init__ (self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex   
    def personInfo (self):
        print('%s,性别：%s,年龄：%d'%(self.name,self.sex,self.age))
        
  
class Teacher(Person):    
    def __init__ (self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
        
    def personInfo (self):
        super().personInfo()
        print('是%s%s的老师'%(self.college,self.professional))
        
    def teachObj (self):
        return '今天讲了如何用面向对象设计程序'
        
        
class Student(Person):
    data_student=[]
    
    def data (self):
        Student.data_student.append('姓名:%s, 年龄:%d, 性别:%s, 学院:%s,专业:%s'%(self.name,self.age,self.sex,self.college,self.professional))
    
    def __init__ (self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
        Student.data(self)
    
    def personInfo (self):
        super().personInfo()
        print('是%s%s的学生'%(self.college,self.sex))
        
    def study (self):
        print('老师%s,我终于学会了！'%Teacher.teachObj(self))
        
        
    def __str__ (self):
        return '%s是%s%s的一位%d岁的%s同学'%(self.name,self.college,self.sex,self.age,self.sex)
        
        
    
a=Student('柏春宇',18,'男','信息与工程','信息管理与信息系统')
a.personInfo()
a.study()
d=Teacher('陈功锁',44,'男','信息与工程','信息管理与信息系统')
d.personInfo()

