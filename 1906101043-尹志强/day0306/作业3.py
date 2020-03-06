class Person():
    def __init__(self,name,age,gender):
       self.name=name
       self.age=age
       self.gender=gender
    def personInfo(self):
        print('我的姓名：%s,年龄:%d,性别：%s'%(self.name,self.age,self.gender))


class Teacher(Person):
    def __init__(self,name,age,gender,college,perofessional):
        super().__init__(name,age,gender)
        self.college=college
        self.perofessional=perofessional
    def personInfo(self):
        super().personInfo()
        print('老师叫做%s,年龄:%s,性别%s,他在%s学院，教%s'%(self.name,self.age,self.gender,self.college,self.perofessional))
    def teachObj(self):
        return '今天讲了面对对象'

class Student(Person):
    def __init__(self,name,age,gender,college,class1):
        super().__init__(name,age,gender)
        self.college=college
        self.class1=class1
    def personInfo(self):
        print('我的名字是:%s,今年%s岁，是一个%s生，在%s学习%s'%(self.name,self.age,self.gender,self.college,self.class1))
    def study(self,teacher):
        print('老师%s我终于学会了!'%(teacher.teachObj(self)))
a=Student('尹志强',20,'男','经济学院','经济学')
a.personInfo()
a.study(Teacher)