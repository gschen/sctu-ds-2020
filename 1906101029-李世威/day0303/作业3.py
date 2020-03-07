#创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
class Person():
    def __init__(self,name,age,sex,):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print(self.name,self.age,self.sex)
class Teacher(Person):
    def __init__(self,name,age,sex,collage,professional):
        Person.__init__(self,name,age,sex)
        self.collage=collage
        self.professional=professional
    def personinfo(self):
        super().personinfo()
        print(self.collage,self.professional)
    def teachObj(self):
         print('今天讲了：面向对象设计程序')
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
a=Student('李世威',19,'男','信息与工程学院','19信管01')
a.personinfo()
a.study()