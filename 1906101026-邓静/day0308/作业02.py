#2、创建Teacher类，继承Person类，属性有学院college，专业professional重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
class Teacher(object):
    def __init__(self,name,age,gender,college,professional):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.professional=professional
    def personInfo(self):
        print('%s,%d,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序')
a=Teacher('邓静',19,'女','四川旅游学院','信息管理与信息系统')
a.personInfo()
a.teachObj()
