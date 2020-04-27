class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('姓名',self.name)  
        print('年龄',self.age)
        print('性别',self.gender)
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        Person.__init__(self,name,age,gender)
        self.college=college
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print('学院',self.college)  
        print('专业',self.professional)  
    def teachObj(self):
        return "今天讲了:面向对象设计程序"
class Student(Person):
    def __init__(self,name,age,gender,college,banji):
        Person.__init__(self,name,age,gender)
        self.college=college
        self.banji=banji
    def personInfo(self):
        super().personInfo()
        print('学院',self.college)
        print('班级',self.banji)
    def study(self):
        print("老师%s,我终于学会了!"%Teacher.teachObj(self))
a=Student("邹婷","19岁","女","信息与工程学院","19信管1班")
a.personInfo()
a.study()