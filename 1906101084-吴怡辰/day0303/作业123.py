class Person():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def personInfo(self):
        print(self.name,self.age,self.sex)
a = Person("wuyichen",18,"girl")
a.personInfo()

class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college = college
        self.professional = professional
    def personInfo1(self):
        super().personInfo()
        print(self.college,self.professional)
    def teachObj(self):
        return "今天讲了：面向对象设计程序"
b = Teacher("chengs",35,"male","信工学院","信管专业")
b.personInfo1()
b.teachObj()

class Student(Person):
    def __init__(self,name,age,sex,college,clas):
        super().__init__(name,age,sex)
        self.college = college
        self.clas = clas
    def personInfo2(self):
        super().personInfo()
        print(self.college,self.clas)
    def student(self):
        print("老师{}，我终于学会了！".format(Teacher.teachObj(self)))
c = Student("wuyichen",18,"girl","信工学院","信管3班")
c.personInfo2()
c.student()
