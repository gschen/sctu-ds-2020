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
x = Teacher('张小明',48,'男','四川大学','信息技术')
x.personInfo()
x.teachObj()


