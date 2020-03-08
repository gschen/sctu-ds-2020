class Person():
    def __init__(self,name,ages,sex):
        self.name = name
        self.ages = ages
        self.sex  = sex
    def personInfo(self):
        print("姓名:",self.name)
        print("年龄:",self.ages)
        print("性别:",self.sex)
class Teacher(Person):
    def __init__(self,name,ages,sex,college,professional):
        Person.__init__(self,name,ages,sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print("学院:",self.college)
        print("专业:",self.professional)
    def teachobj(self):
        print("今天讲了：面向对象设计程序")
jams=Teacher("jams",20,"男","信息与工程学院","信息管理与信息系统")
jams.personInfo()
jams.teachobj()

