#2、创建Teacher,继承Person，属性有学院college,专业professional,重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’


class Person():
    def __init__(self,name,age,gender):
        self.name='小米'
        self.age='15岁'
        self.gender='女'
    def personInfo(self):
        print('学生小米，15岁,女')
        print('老师是%s,%s'%(self.m,self.n))
class Teacher(Person):
    def __init__(self):
        self.m='信息与工程学院'
        self.n='信息管理与信息系统'
    def personInfo(self):
        print('信息与管理系统','信息管理与信息系统专业')
    def teachObj(self):
        print('今天讲了:面向对象设计编程')

b=Teacher()
b.teachObj()
super(Teacher,b).personInfo()

