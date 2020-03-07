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
        return "今天讲了：面向对象设计程序"
class Student(Person):
    def __init__(self,n,a,g,xueyuan,banji):
        Person.__init__(self,n,a,g)
        self.xueyuan = xueyuan
        self.banji = banji
    def personInfo(self):
        print("姓名：%s 年龄：%d 性别：%s 学院：%s 班级：%s"%(self.name,self.age,self.gender,self.xueyuan,self.banji))
    def study(self,t):
        print("老师%s,我终于学会了!"%(t.teachObj()))
x = Student('杨嘉玲',18,'女','信息与工程学院','19信管02')
t = Teacher('张小明',48,'男','四川大学','信息技术')
x.personInfo()
x.study(t)
        
        
        
