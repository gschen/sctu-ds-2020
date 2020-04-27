class Person():
    def __init__(self):
        self.name="李木子"
        self.age="20岁"
        self.gender="女"
		self.college="信息与工程学院"
		self.professional="信息管理与信息系统"
    def personInfo(self):
            print("学生是李木子，20岁，女，学院是信管与工程学院，专业是信息管理与信息系统")
            print("老师是%s,%s" % (self.x,self.z))
class Teacher(Person):
    def __init__(self):
        self.x="信息与工程学院"
        self.z="信息管理与信息系统专业"
    def personInfo(self):
        print("信息与工程学院","信息管理与信息系统专业")
    def teachObj(self):
        print("今天讲了：面向对象设计程序")
b=Teacher()
b.teachObj()
super(Teacher,b).personInfo()