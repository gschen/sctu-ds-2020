# 2、创建Teacher类，继承Person类，属性有学院college，专业professional
# ，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序
class person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名：',self.name,'年龄：',self.age,'性别：',self.sex)

class Teacher(person):
    def __init__(self,college,professional,comment):
        self.college=college
        self.professional=professional
        self.comment=comment
        
    def teach0bj(self):
        print(self.comment)

a=person('李华',18,'男')
b=Teacher('信息工程学院','信息管理与信息系统','‘今天讲了：面向对象设计程序’')
b.personInfo()
b.teach0bj()