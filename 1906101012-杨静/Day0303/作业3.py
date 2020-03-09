"""
创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，
调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，
接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
"""
class Student(Person):
    def __init__(self):
        self.classs = '19信管01'
        self.college = '信息与工程'
        super(Student, self).__init__()
    def personInfo(self):
        print('class:%s\n collage:%s' % (self.classs,self.college))
        super(Student,self).personInfo()
    def study(self):
        print('老师,%s,我终于学会了！' % b.professional)
c = Student()   
Student.personInfo(c)
c.study()