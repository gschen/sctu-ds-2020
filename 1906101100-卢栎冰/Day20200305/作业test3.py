# 3.创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，
# 将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，
# 接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。

class Person(object):
    def personInfo(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        return self.name,self.age,self.sex
class Teach(Person):
    def personInfo(self,name,age,sex,college,professional):
        self.name=name
        self.age=age
        self.sex=sex
        self.college=college
        self.professional=professional
        return self.name,self.age,self.sex,self.college,self.professional
class Student(Person):
    def personInfo(self,name,age,sex,college,classroom):
        self.name=name
        self.age=age
        self.sex=sex
        self.college=college
        self.classroom=classroom
        return self.name,self.age,self.sex,self.college,self.classroom
    def study(self):
        return '老师xxx,我终于学会了！'
# a=Student
# print(a.personInfo('小鹿','19','女','信工学院','12'))
# print(a.study())