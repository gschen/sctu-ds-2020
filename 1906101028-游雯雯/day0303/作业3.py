class Person():
    def __init__(self,name,age,gender):
        self.name="Kyle"
        self.age="19岁"
        self.gender="男"
    def personInfo(self):
        print("学生是Kyle,18岁，男")
        print("老师是%s,%s"%(self.college,self.class1))
    class Teacher(Person):
        def __init__(self):
            self.m="sctu"
            self.n="信息管理与信息系统"
        def teachObj(self,object):
            print("今天讲了：面向对象设计程序")
class Student(Person):
    def __init__(self):
        self.college="信息与工程学院"
        self.class1="19信管01"
    def personInfo(self):
        print("sctu")
    def study(self,object):
        print("老师%s,我终于学会了！"%(object.teschObj))
y=Teacher()
x=Student()
x.study(y)
super(Student,x).personInfo()