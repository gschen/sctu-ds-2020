class Person():
    def __init__(self):
        self.name='常琳'
        self.age=19
        self.sex='女'
        self.class1='信管3班'
        self.academy='信息与工程学院'
    def Personinfo(self):
        print('姓名：%s,年龄：%s,性别：%s,班级：%s,学院：%s'%(self.name,self.age,self.sex,self.class1,self.academy))
class Student(Person):
    def __init__(self):
        Person.__init__(self)
    def rest(self):
        Person.Personinfo(self)
a=Student()
a.rest()

class Teacher():
    def __init__(self):
        self.today='今天讲了，面向对象的编程'
    def teacherobj(self):
        print(self.today)
class Study(Teacher):
    def workon(self):
        print('老师,我终于学会了')
b=Teacher()
b.teacherobj()
c=Study()
c.workon()