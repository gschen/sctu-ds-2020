#第一题
class Person():
    def __init__(self,name,age,sexuality):
        self.name = name
        self.age = age
        self.sexuality = sexuality
    def printInfo(self):
        print("在下唤——%s,%s岁，%s。" % 
        (self.name,self.age,self.sexuality))
#第二题
class Teacher(Person):
    def __init__(self,name,age,sexuality,college,professional):
        self.name = name
        self.age = age
        self.sexuality = sexuality
        self.college = college
        self.professional = professional
    def printInfo(self):
        print("在下唤——%s,%s岁，%s，%s,%s" % 
        (self.name,self.age,self.sexuality,self.college,self.professional))
    def teachobj(self,teacher):
        print ("今天%s讲了：面向对象设计程序" % (self.name))
 #第三题
class Student(Person):
    def __init__(self,name,age,sexuality,college,Class):
        self.name = name
        self.age = age
        self.sexuality = sexuality
        self.college = college
        self.Class = Class
    def printInfo(self):
        print("在下唤——%s,%s岁，%s，%s,%s" % 
        (self.name,self.age,self.sexuality,self.college,self.Class))
    def study(self):
        print('老师,%s,我终于学会了！')
    def teach(self):
        return 'python'
someone = Person('吴钩','38','男')
teacher = Teacher('东皇','46','男','信息工程学院','信息系统与信息管理')
onestudent = Student('林木','19','男','信息工程学院','三班')
someone.printInfo()
teacher.printInfo()
teacher.teachobj(Teacher)
onestudent.printInfo()








