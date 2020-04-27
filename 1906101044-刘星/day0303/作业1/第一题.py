#创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('name:%s,age:%s,sex:%s'%(self.name,self.age,self.sex))

#创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
class Teacher(Person):
    def __init__(self,name,age,sex,collega,professional):
        Person.__init__(self,name,age,sex)
        self.collega=collega
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('collega:%s,professional:%s'%(self.collega,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序')
xinxi=Teacher('Mary',25,'女','信息与工程学院','信息管理与信息系统')
xinxi.personInfo()
xinxi.teachObj()


#创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
#创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
class Student(Person):
    def __init__(self,name,age,sex,collega,banji):
        Person.__init__(self,name,age,sex)
        self.collega=collega
        self.banji=banji
    def personInfo1(self):
        super().personInfo()
        print('collega:%s,banji:%s'%(self.collega,self.banji))
    def study(self):
        print('老师%s，我终于学会了！'%Teacher.teachObj(self))
a=Student('刘星',20,'女','信息与工程学院','信管2班')
a.personInfo1()
a.study()