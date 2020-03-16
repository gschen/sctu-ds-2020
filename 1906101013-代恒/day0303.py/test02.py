class Person():
    def __init__(self):
        self.name = "代恒"
        self.age = 18
        self.sex = "nan"
    def personInfo(self):
        return self.name,self.age,self.sex


class Teacher(Person):
    def __init__(self):
        self.college = '旅游学院'
        self.professional = '信息管理与信息系统'
    def personInfo(self):
        return self.name,self.age,self.sex,self.collage,self.professional
    def teachobj(self):
        self.d = '今天讲了：面向对象设计程序'
        return self.d

a=Teacher()
a.teachobj()
super(Teacher,a).personInfo()
