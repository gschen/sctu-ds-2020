
#第一种方法
class Person():
    def __init__(self):
        self.name = "肖文星"
        self.age = 19
        self.gender = "male"
        self.class_ = "信管01"
        self.college = "信息与工程学院"
    def personInfo(self):
        return self.name,self.age,self.gender,self.class_,self.college
class Student(Person):
    def __init__(self):
        Person.__init__(self)
    def another(self):
        Person.personInfo(self)
a = Student()
print(super(Student,a).personInfo())

#第二种方法
class Person1():
    def __init__(self):
        self.name = "肖文星"
        self.age = 19
        self.gender = "male"
        self.class_ = "信管01"
        self.college = "信息与工程学院"
    def personInfo(self):
        return self.name,self.age,self.gender,self.class_,self.college
class Student1(Person1):
    def another(self):
        return Person1.personInfo(self)
        
b = Student1()
print(b.another())

class Teacher():
    def __init__(self):
        self.today = "今天讲了类"
    def teacherObj(self):
        return self.today
class study(Teacher):
    def work(self):
        return "老师{}，我终于学会了".format(Teacher.teacherObj(self))

c = study()
print(c.work())