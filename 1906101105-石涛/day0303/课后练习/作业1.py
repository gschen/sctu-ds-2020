# coding=utf-8

'''
1、	创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
'''
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名：{}\n年龄：{}\n性别：{}'.format(self.name,self.age,self.sex))

xaioming=Person('小明',19,'男')
xaioming.personInfo()


print('\n','-'*10,'\n')

'''
2、	创建Teacher类，继承Person类，属性有学院college，专业professional
，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。
创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
'''
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        print('姓名：{}\n年龄：{}\n性别：{}\n学院：{}\n专业：{}'.format(self.name,self.age,self.sex,self.college,self.professional))
    def teachobj(self):
        return('今天讲了：面向对象设计程序')

chen=Teacher('陈',28,'男','sctu','信管')
chen.personInfo()
print(chen.teachobj())


print('\n','-'*10,'\n')

'''
3、   创建Student类，继承Person类，属性有学院college，班级class，重写
父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息
也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，
接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
'''
class Student(Person):
    def __init__(self,name,age,sex,college,classes):
        super().__init__(name,age,sex)
        self.college=college
        self.classes=classes
    def personInfo(self):
        print('姓名：{}\n年龄：{}\n性别：{}\n学院：{}\n班级：{}'.format(self.name,self.age,self.sex,self.college,self.classes))
    def study(self,knowledge):
        print('老师，{}，我终于学会了！'.format(knowledge))

st=Student('ST-one',19,'男','sctu','信管')
st.personInfo()
st.study(str(chen.teachobj())[5:])