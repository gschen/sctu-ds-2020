# 3、   创建Student类，继承Person类，属性有学院college，班级class，
# 重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
# 创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，
# 然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。

class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('姓名:%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender)) 
class Student(Person):
    def __init__(self,name,age,gender,college,myclass):
        super().__init__(name,age,gender)
        self.college=college
        self.myclass=myclass
    def personInfo(self):
        super().personInfo()
        print('我是%s%s的学生'%(self.college,self.myclass))
    def study(self,teacher):
        print('我是%s,老师%s,我终于学会了!'%(self.name,teacher.teachObj()))
    def __str__(self):
        return '我是一名叫做%s的学生,我的年龄是:%d,我的性别是:%s'%(self.name,self,age,self.gender)   
s=Student('tracy',18,'女','四川旅游学院','信管3班')                                                                          
s.personInfo()
s.study