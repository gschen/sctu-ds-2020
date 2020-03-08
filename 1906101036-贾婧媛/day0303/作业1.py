#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,
#打印这个人的信息
#2、创建Teacher类，继承Person类，属性有学院college，专业professional
#重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也
#打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
#3、创建Student类，继承Person类，属性有学院college，班级class，重写
# 父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级
# 信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的
# teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会
# 了！’xxx为老师的teach方法返回的信息。

class Person():
    def __init__(self):
        self.name='贾婧媛'
        self.age=18
        self.gender='女'
        super(Person,self).__init__()
    def personInfo(self):
        print('name:%s\nage:%s\ngender:%s'%(self.name,self.age,self.gender))
a=Person()
Person.personInfo(a)


class Teacher(Person):
    def __init__(self):
        self.college='信息与工程学院'
        self.professional='信息管理与信息系统'
        self.course='面向对象程序设计'
        super(Teacher,self).__init__()
    def personInfo(self):
        print('college:%s\nprofessional:%s'%(self.college,self.professional))
        super(Teacher,self).personInfo()
    def teachObj(self):
        print('今天讲了:%s'%self.course)
b=Teacher()
Teacher.personInfo(b)
b.teachObj()


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

