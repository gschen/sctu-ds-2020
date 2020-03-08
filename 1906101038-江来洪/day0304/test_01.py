class Person():
    def __init__(self):
        self.name = 'jianglaihong'
        self.age = 19
        self.gender = '男'
        super(Person,self).__init__()
    def personInfo(self):
        print('name:%s\nage:%s\ngender:%s' % (self.name,self.age,self.gender))
print('第一题-person')
a = Person()
Person.personInfo(a)
print('\n')
class Teacher(Person):
    def __init__(self):
        self.college = '信息与工程'
        self.professional = '信息管理与信息系统'
        self.content = '面向对象设计程序'
        super(Teacher,self).__init__()
    def personInfo(self):
        print('college:%s\nprofessional:%s' % (self.college,self.professional))
        super(Teacher,self).personInfo()
    def teach0bj(self):
        print('今天讲了:%s' % self.content)
print('第二题-teacher')
b = Teacher()
Teacher.personInfo(b)
b.teach0bj()
print('\n')
class Student(Person):
    def __init__(self):
        self.classs = '19信管01'
        self.college = '信息与工程'
        super(Student, self).__init__()
    def personInfo(self):
        print('class:%s\ncoleeg:%s' % (self.classs,self.college))
        super(Student,self).personInfo()
    def study(self):
        print('老师,%s,我终于学会了！' % b.content)
print('第三题-student')
c = Student()
Student.personInfo(c)
c.study()


