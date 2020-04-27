# 2.创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法
# 除打印个人信息外，将老师的学院、专业信息也打印出来
# 创建teachObj方法，返回信息为“今天讲了：面向对象设计程序”
class Person():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college = college
        self.professional = professional
    def personInfo(self):
        print("姓名：%s,年龄：%s,性别:%s,学院:%s,专业:%s" % (self.name,self.age,self.sex,self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象程序设计'

a = Teacher('张三',39,'男','信息与工程学院','信管专业')
a.personInfo()
print(a.teachObj())