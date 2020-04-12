#	创建Teacher类，继承Person类，属性有学院college，专业professional
#重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
class Person():
    def __init__(self):
        self.name = "唐鹏凯"
        self.age = 18
        self.gender = "male"
        self.college = "信息与工程学院"
        self.professional = "信息管理与信息系统"
    def personInfo(self):
        return "name:{},age:{},gender:{},college:{},professional:{}".format(self.name,self.age,self.gender,self.college,self.professional)
class Teacher(Person):
    def __init__(self):
        Person.__init__(self)
        self.today = "今天讲了：‘面向对象编程’"
    def teacherObj(self):
        return self.today

a = Teacher()
print(a.teacherObj())
print(super(Teacher,a).personInfo())
