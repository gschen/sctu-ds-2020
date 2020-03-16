#第一种方法
class Person():
    def __init__(self):
        self.name = "贾佳"
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
class Person():
    def __init__(self):
        self.name = "贾佳"
        self.age = 19
        self.gender = "male"
        self.class_ = "信管01"
        self.college = "信息与工程学院"
    def personInfo(self):
        return self.name,self.age,self.gender,self.class_,self.college
class Student(Person):
    def another(self):
        return Person.personInfo(self)
        
b = Student()
print(b.another())

class Teacher():
    def __init__(self):
        self.today = "今天讲了：‘面向对象编程’"
    def teacherObj(self):
        return self.today
class study(Teacher):
    def work(self):
        return "老师{}，我终于学会了".format(Teacher.teacherObj(self))

c = study()
print(c.work())
