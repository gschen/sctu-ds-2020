class Person():
    def __init__(self):
        self.name = "余春江"
        self.age = 18
        self.gender = "male"
        self.college = "信息与工程学院"
        self.professional = "信息管理与信息系统"
    def personInfo(self):
        return "name:{},age:{},gender:{},college:{},professional:{}".format(self.name,self.age,self.gender,self.college,self.professional)
class Teacher(Person):
    def __init__(self):
        Person.__init__(self)
        self.today = "‘面向对象编程’"
    def teacherObj(self):
        return self.today

a = Teacher()
print(a.teacherObj())
print(super(Teacher,a).personInfo())
