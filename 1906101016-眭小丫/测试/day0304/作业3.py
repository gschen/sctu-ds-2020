# 创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
class Person(object):
    def _init_(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('我叫%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender))

class Teacher(Person):
    def _init_(self,name,age,gender,college,personInfo):
        super()._init_(name,age,gender)
        self.college=college
        self.personInfo=personInfo
    #def personInfo(self):
        super().personInfo()
        print('是%s%s的老师'%(self.college,self.personInfo))
    def teachobj(self):
        return '今天讲了：面向对象程序设计'

class Student(Person):
    data_student=[]
    def data(self):
        Student.data_student.append('姓名：%s,年龄：%d,性别：%s,学院：%s,班级:%s'%(self.name,self.age,self.gender,self.college,self.banji))
    def _init_(self,name,age,gender,college,banji):
        super()._init_(name,age,gender)
        self.college=college
        self.banji=banji
        Student.data(self)
    def personInfo(self):
        super().personInfo()
        print('是%s%s的学生'%(self.college,self.banji))
    def study(self):
        print('老师%s,我终于学会了！'%Teacher.teachobj(self))
    def _str_(self):
        return ('%s是%s%s的一位%d岁的%s同学'%(self.name,self.college,self.banji,self.age,self.gender))

