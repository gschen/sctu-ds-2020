class Person():
    def __init__(self,name,age,gender):
        self.name="小明"
        self.age="17岁"
        self.gender="女"
    def personInfo(self):
            print("学生：小明，17岁，女")
            print("老师是%s,%s"%(self.m,self.n))
class Teacher(Person):
    def __init__(self):
        self.m="信息与工程学院"
        self.n="信息管理与信息系统专业"
    def personInfo(self):
        print("信息与工程学院","信息管理与信息系统专业")
    def teachObj(self):
        print("今天讲了：面向对象设计程序")
b=Teacher()
b.teachObj()
super(Teacher,b).personInfo()