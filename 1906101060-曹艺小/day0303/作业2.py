#第二题
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        print("姓名：%s,年龄：%s,性别:%s,学院:%s,专业:%s" % (self.name,self.age,self.sex,self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象程序设计'

a=Teacher('David',40,'男','信息与工程学院','信管专业')
a.personInfo()
print(a.teachObj())