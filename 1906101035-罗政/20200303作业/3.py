lass Person():
    def __init__(self):
        self.name = "罗政"
        self.age = 19
        self.gender = "male"
        self.class_ = "信管1"
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