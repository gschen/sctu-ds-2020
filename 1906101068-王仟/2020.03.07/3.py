class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print("姓名",self.name)
        print("年龄",self.age)
        print("性别",self.sex)
class Teacher(Person):
        def __init__(self,name,age,sex,collage,professional):
            Person.__init__(self,name,age,sex)
            self.collage=collage
            self.professional=professional
        def personinfo(self):
            super().personinfo()
            print("学院",self.collage)
            print("专业",self,professional)
        def teachobj(self):
            return "今天讲了：面向对象程序设计"
class Student(Person):
        def __init__(self,name,age,sex,collage,classroom):
            Person.__init__(self,name,age,sex)
            self.collage=collage
            self.classroom=classroom
        def personinfo(self):
            super().personinfo()
            print("学院",self.collage)
            print("班级",self.classroom)
        def study(self):
            print("老师%s,今天我终于学会了"%(Teacher.teachobj(self)))
a=Student("qw",19,"女","信息与工程学院","19信管2班")
a.personinfo()
a.study()
