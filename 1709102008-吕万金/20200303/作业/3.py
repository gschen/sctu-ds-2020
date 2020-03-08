#3、   创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional
    def personInfo(self):
        print("姓名：%s,年龄:%s,性别:%s,学院：%s,专业：%s" % (self.name,self.age,self.gender,self.college,self.professional))
    def teachObj(self):
        return '今天讲了：面向对象设计程序'
class Student(Person):
    def __init__(self,name,age,gender,college,grade):
        super().__init__(name,age,gender)
        self.college=college
        self.grade=grade
    def personInfo(self):
        print("姓名：%s,年龄:%s,性别:%s,学院：%s,班级：%s" % (self.name,self.age,self.gender,self.college,self.grade))
    def study(self,Teacher):
        print('老师%s,我终于学会了！'%(Teacher.teachObj(self)))
a=Student('吕万金',18,'女','信息','2班')
a.personInfo()
a.study(Teacher)