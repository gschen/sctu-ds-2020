class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    
    def personInfo(self):
        print(self.name,self.age,self.sex)

XiaoM=Person('王小明','18岁','男')
XiaoM.personInfo()

class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)  #等同于 self.name=name，self.age=age，self.sex=sex
    
        self.college=college
        self.professional
      
    def personInfo(self):
        print(self.name,self.age,self.sex,self.college,self.professional)

    def teachobj(self):
        return '今天讲了：面向对象程序设计'

laoc=Teacher('陈老师','32岁','信工学院','信息管理与信息系统')
laoc.personInfo()


class Student(Person):
    def __init__(self,name,age,sex,college,class1):
        super().__init__(name,age,sex)
        
        self.collage=college
        self.class1=class1
    def personInfo(self):
        print('我叫%s,年龄%s，性别%s，学院%s，班级%s'%(self.name,self.age,self.sex,self.collage,self.class1))
    def study(self,object):
        recept=object.teachobj()
        print('老师{}，我终于学会了'.format(recept))


laog=Student('小明','18岁','男','信工学院',3)
laog.study(laoc)