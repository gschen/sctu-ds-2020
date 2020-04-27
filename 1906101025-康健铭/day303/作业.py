# class Person():
#     def __init__(self):
#         self.name = "kjm"
#         self.age = 19
#         self.gender = "male"
#     def personInfo(self):
#         return self.name, self.age, self.gender


# a = Person()
# print(a.personInfo())



# class Person():
#     def __init__(self):
#         self.name = "kjm"
#         self.age = 19
#         self.gender = "male"
#         self.college = "信息与工程学院"
#         self.professional = "信息管理与信息系统"
#     def personInfo(self):
#         return "name:{}, age:{}, gender:{}, college:{}, professional:{}".format(self.name, self.age, self.gender, self.college, self.professional)
# class Teacher(Person):
#     def __init__(self):
#         Person.__init__(self)
#         self.today = "今天讲了新知识"
#     def teacherObj(self):
#         return self.today

# a = Teacher()
# print(a.teacherObj())
# print(super(Teacher, a).personInfo())




# class Person():
#     def __init__(self):
#         self.name = "kjm"
#         self.age = 19
#         self.gender = "male"
#         self.class_ = "信管01"
#         self.college = "信息与工程学院"
#     def personInfo(self):
#         return self.name, self.age, self.gender, self.class_, self.college


# class Student(Person):
#     def __init__(self):
#         Person.__init__(self)
#     def another(self):
#         Person.personInfo(self)


# a = Student()
# print(super(Student,a).personInfo())
