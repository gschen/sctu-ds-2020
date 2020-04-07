# 2、创建Teacher类，继承Person类，属性有学院college，专业professional
# ，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。
# 创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’

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
    def teachObj(self):
        return '今天讲了：面向程序设计'
a=Teach()
print(a.personInfo('小鹿','19','女','信工学院','信管'))
print(a.teachObj())