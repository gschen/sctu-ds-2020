'''2、	创建Teacher类，继承Person类，属性有学院college，专业professional,重写父类
personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，
返回信息为‘今天讲了：面向对象设计程序’'''
class Person():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def personInfo(self):
        print('我叫%s,年龄%s,性别%s'%(self.name,self.age,self.sex))
x=Person('杨超',19,'男')
x.personInfo()
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college = college
        self.professional = professional
    def personInfo(self):
        print('%s,%s,%s,%s,%s'%(self.name,self.age,self.sex,self.college,self.professional))
    def teachObj(self):
        return ('今天讲了：面向对象设计程序')
y = Teacher('gongsuochen',36,'男','信息与工程学院','程序设计')
y.personInfo()
print(y.teachObj())
    
