class person():
    def __init__(self,name,age,gender):
        self.name='张三'
        self.age='20岁'
        self.gender='女' 
    def personInfo(self):
            print('学生是张三，20岁，女')
            print('老师是%s,%s'%(self.college,self.class1))
class teacher(person):
    def __init__(self):
        self.x='信息与工程学院'
        self.z='信息管理与信息系统'
    def  teachObj(self,object):
            print('今天讲了：面向对象设计编程')
class student(person):
    def __init__(self):
        self.college='信息与工程学院'
        self.class1='19信管03'
    def personInfo(self):
            print('sctu')
    def study(self,object):
            print('老师%s,我终于学会了!'% (object.teachObj))
y=teacher()
x=student()
x.study(y)
super(student,x).personInfo()            

