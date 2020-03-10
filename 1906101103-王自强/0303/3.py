class Person(object):
    def personInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        return self.name, self.age, self.sex


class Teacher(Person):
    def personInfo(self, name, age, sex, college, professional):
        self.name = name
        self.age = age
        self.sex = sex
        self.college = college
        self.professional = professional
        return self.name, self.age, self.sex, self.college, self.professional

    def teachObj(self):
        return '今天讲了：面向对象设计程序'


class Student(Person):
    def personInfo(self, college, class1):
        self.class1 = class1
        self.college = college

        return self.college, self.class1

    def study(self, object):
        return '老师%s,我终于学会了！' % object.teachObj()


a = Student()
print(a.personInfo('战神学院', 11))
print(super(Student, a).personInfo('小明', 18, '男'))
b = Teacher()
print(a.study(b))

