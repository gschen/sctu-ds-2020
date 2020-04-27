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

    def study(self,object):
        recept=object.teachObj()
        print('老师{},我终于学会了！'.format(recept))

laoF=Student('王二',20,'男','信工学院',1)
laoF.study(laoC)