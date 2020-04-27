#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('我叫%s,年龄:%s,性别:%s'%(self.name,self.age,self.gender))
#2、创建Teacher类，继承Person类，属性有学院college，专业professional，
#重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’

class Techer(Person):
    def __init__(self,name,age,gender,college,professional):
        self.name=name  #super().__init__(name,age,gender)
        self.age=age    #可用这个调用作业1的代码，避免重复
        self.gender=gender
        self.college=college
        self.professional=professional
    def personInfo(self):
        print('我叫%s,年龄:%s,性别:%s,我是来自%s的一名%s老师'%(self.name,self.age,self.gender，self.college,self.professional))
    def teach(self):
        return'今天讲了：面向对象设计程序'
#创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，
# 调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，
# 接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。


class Student(Person):
    def __init__(self,name,age,gender,college,班级):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.班级=班级
    def personInfo(self):
        print('我叫%s,年龄:%s,性别:%s,我是%s的%s班的学生'%(self.name,self.age,self.gender，self.college,self.班级))

    def study(self,teacher):
        print('我是%s,老师%s,我终于学会了！'%(self.name,self.age,self.gender，self.college,self.班级))
