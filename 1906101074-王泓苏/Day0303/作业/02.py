# 2、创建Teacher类，继承Person类，属性有学院college，专业professional，
# 重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。
# 创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名:',self.name)
        print('年龄:',self.age)
        print('性别:',self.sex)
class Teacher(Person):
    def __init__(self,name,age,sex,collage,professional):
        super().__init__(name,age,sex)
        self.collage=collage
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('学院:',self.collage)
        print('专业:',self.professional)
    def teachobj(self):
        print('今天讲了：面向对象设计程序')
a=Teacher('Tom',30,'男','信息与工程学院','信息管理与信息系统')
a.personInfo()
a.teachobj()
