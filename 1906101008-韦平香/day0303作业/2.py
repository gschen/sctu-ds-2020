#2、	创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。
# 创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
#
class Person():
    def __init__(self,name,age,gender):
        self.name="李小"
        self.age="18岁"
        self.gender="男"
    def personInfo(self):
            print("学生是李小，18岁，男")
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