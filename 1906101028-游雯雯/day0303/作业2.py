class Person():
    def __init__(self,name,age,gender):
        self.name="Chole"
        self.age="22岁"
        self.gender="女"
    def personInfo(self):
        print("学生是Chole，22岁，女")
        print("老师是%s,%s"%(self.m,self.n))
class Teacher(Person):
    def __init__(self):
        self.m="信息与工程学院"
        self.n="信息管理与信息系统"
    def personInfo(self):
        print("信息与工程学院","信息管理与信息系统")
    def teachObj(self):
        print("今天讲了：面向对象设计程序")
b=Teacher()
b.teachObj()
super(Teacher,b).personInfo()