# 2、创建Teacher类，继承Person类，属性有学院college，专业professional
# ，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。
# 创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’

class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('姓名:%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender)) 
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('我是来自%s%s的一名讲师'%(self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象设计程序'

teacher=Teacher('jack',20,'男','四川旅游学院','信息与工程学院')                                                                          
teacher.personInfo()
teacher.teachObj