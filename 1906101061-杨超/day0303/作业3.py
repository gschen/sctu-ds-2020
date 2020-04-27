'''创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用
父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调
用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师
的teach方法返回的信息。'''
class Person():
    def __init__(self):
        self.name = "杨超"
        self.age = 19
        self.sex = "男"
        self.class_ = "信管2班"
        self.college = "信息与工程学院"
    def personInfo(self):
        return self.name, self.age, self.sex, self.class_, self.college


class Student(Person):
    def another(self):
        return Person.personInfo(self)


b = Student()
print(b.another())


class Teacher():
    def __init__(self):
        self.today = "今天"
    def teacherObj(self):
        return self.today
class study(Teacher):
    def work(self):
        return "{}终于学会了".format(Teacher.teacherObj(self))


c = study()
print(c.work())