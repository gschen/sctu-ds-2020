#创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。

class Person():
    def __init__(self,name,age,gender):
        self.name="李小"
        self.age="18岁"
        self.gender="男"
    def personInfo(self):
            print("学生是李小，18岁，男")
class Teacher(Person):
    def __init__(self):
        self.m="sctu"
        self.n="信息管理与信息系统"
    def teachObj(self,object):
        print("今天讲了：面向对象设计程序")
class Student(Person):
    def __init__(self):
        self.college="信息与工程学院"
        self.class1="19信管01"
    def personInfo(self):
            print("sctu")
    def study(self,object):
            print("老师%s，我终于学会了！"% (object.teachObj))
y=Teacher()
x=Student()
x.study(y)
super(Student,x).personInfo()