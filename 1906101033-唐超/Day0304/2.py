# 2、	创建Teacher类，继承Person类，属性有学院college，专业professional，重
# 写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。
# 创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’

class Person:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
    def personInfo(self):
        print("姓名：%s 年龄:%d 性别:%s"%(self.name,self.age,self.gender))
class Teacher(Person):
    def __init__(self,n,a,g,college,professional):
        Person.__init__(self,n,a,g)
        self.college = college
        self.professional = professional
    def personInfo(self):
        print("姓名：%s 年龄:%d 性别:%s \n老师的学院：%s 专业信息:%s"%(self.name,self.age,self.gender,self.college,self.professional))
    def teachObj(self):
        print("今天讲了：面向对象设计程序")
x = Teacher('李四',20,'男','四川旅游大学','信息管理与信息系统')
x.personInfo()
x.teachObj()