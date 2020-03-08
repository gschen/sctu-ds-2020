#  创建Student类，继承Person类，属性有学院college，班级class，
# 重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
# 创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，
# 然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。

class Person(object):
    def personInfo(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        return self.name,self.age,self.sex
class Teacher(Person):
    def personInfo(self,name,age,sex,college,professional):
        self.name=name
        self.age=age
        self.sex=sex
        self.college=college
        self.professional=professional
        return self.name,self.age,self.sex,self.college,self.professional
    def teachObj(self):
        return '今天讲了：面向对象设计程序'
class Student(Person):
    def personInfo(self,college,class1):
        self.class1=class1
        self.college=college
        
        return self.college,self.class1
    def study(self,object):
        return '老师%s,我终于学会了！'%object.teachObj()
a=Student()
print(a.personInfo('战神学院',11))
print(super(Student,a).personInfo('小明',18,'男'))
b=Teacher()
print(a.study(b))


    
