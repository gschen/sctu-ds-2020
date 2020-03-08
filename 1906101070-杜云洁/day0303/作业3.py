# #创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的
# 学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印
# ‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
# 1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print('我是%s,年龄:%d,性别:%s' % (self.name, self.age, self.sex))


class Teacher(Person):
    def __init__(self, name, age, sex, college, professional):
        super().__init__(name, age, sex)
        self.college = college
        self.professional = professional

    def personInfo(self):
        super().personInfo()
        print('我是一名来自%s学院%s专业的老师' % (self.college, self.professional))

    def teachObj(self):
        return ('今天讲了：面向对象设计程序')


class Student(Person):
    def __init__(self, name, age, sex, college, myclass):
        super().__init__(name, age, sex)
        self.college = college
        self.myclass = myclass

    def personInfo(self):
        super().personInfo()
        print('我是一名来自%s%s专业的学生' % (self.college, self.myclass))

    def study(self, tescher):
        print('老师%s,我终于学会了!' % (teacher.teachObj()))

    def __str__(self):
        return '我是一名叫做%s的学生,年龄:%d,性别:%s' % (self.name, self.age, self.sex)


stu1 = Student('张三', 19, '男', '信息与工程学院', '信息管理与信息系统')
stu1.personInfo()
teacher = Teacher('H', 30, '男', '信息与工程学院', '信息管理与信息系统')
teacher.personInfo()
stu1.study(teacher)
stus = []
stus.append(stu1)




