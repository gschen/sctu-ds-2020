class person():
    def __init__(self,name,age,sex):
        self.name="lisa"
        self.age= 19
        self.sex="女"
    def personinfo(self):
        print("lisa",19,"女")
class teacher(person):
    def __init__(self):
        self.collage="信息与工程学院"
        self.major="信息管理与信息系统"
    def teachobj(self,object):
        print("今天讲了，面向对象设计")
class student(person):
    def __init__(self):
        self.Class="19信管01"
    def personinfo(self):
        print("信息与工程学院")
    def teach(self,object):
        print("老师%s,我终于学会了！"%(object.teachobj))
h=teacher()
l=student()
l.teach(h)
super(student,l).personinfo()
