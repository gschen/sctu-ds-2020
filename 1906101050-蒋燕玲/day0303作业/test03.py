#3、   创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名：%s   年龄：%s   性别：%s' %(self.name,self.age,self.sex))
class Teacher(Person):
    def __init__(self,name,sex,age,collage,professional):
        Person .__init__ (self,name,sex,age)
        self.collage=collage
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('学院：%s   专业：%s' %(self.collage,self.professional))
    def teschObj(self):
        return "今天讲了面向对象设计程序"
class Student(Person):
    def __init__(self,name,sex,age,collage,class1):
        Person .__init__ (self,name,sex,age)
        self.collage=collage
        self.class1=class1
    def personInfo(self):
        super().personInfo()
        print('学院：%s   班级：%s' %(self.collage,self.class1))
    def study(self):
        print('老师%s,我终于学会了！' %(Teacher.teschObj(self)))
student1=Student('张三','19','男','信息与工程学院','19信管2班')
student1.personInfo()
student1.study()