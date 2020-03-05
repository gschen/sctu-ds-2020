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
        return "今天讲了：面向对象设计程序"
class Student(Person):
    def __init__(self,name,ages,sex,college,class1):
        Person.__init__(self,name,ages,sex)
        self.college=college
        self.class1=class1
    def personInfo(self):
        super().personInfo()
        print("学院:",self.college)
        print("班级:",self.class1)
    def study(self):
        print("老师%s,我终于学会了"%Teacher.teachobj(self))
jams=Student("jams",20,"男","信息与工程学院","信管03")
jams.personInfo()
jams.study()