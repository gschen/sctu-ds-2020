# #2、创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，除打印个人信息外，将老师的
# 学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('我是%s,年龄:%d,性别:%s'%(self.name,self.age,self.sex))
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('我是一名来自%s学院%s专业的老师'%(self.college,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序!')
person=Person('张三',19,'男')
person.personInfo()
H=Teacher('H',30,'男','信息与工程学院','信息管理与信息系统')
H.personInfo()
H.teachObj()

