# 创建Student类，继承Person类，属性有学院college，班级class，
# 重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
# 创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，
# 然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。


class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
            print(self.name,self.age,self.gender)
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        self.college=college
        self.professional=professional
        super().__init__(name,age,gender)
    def teachObj(self):
        print("今天讲了：面向对象设计程序")
    def personInfo(self):
            print(self.name,self.age,self.gender,self.college,self.professional)
m=Teacher("陈老师",32,"男","信工学院","信息管理与信息系统")
class Student(Person):
    def __init__(self,name,age,gender,college,classzhou):
        super().__init__(name,age,gender)
        self.college=college
        self.classzhou=classzhou
    def personInfo(self):
        def personInfo(self):
            print(self.name,self.age,self.gender,self.college,self.classzhou)
    def study(self,object):
        recept=object.teachObj()
        print("老师{}，我终于学会了！".format(recept))
n=Student("林以信",20,"男","信工学院",3)
n.study(m)