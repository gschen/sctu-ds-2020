class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(self.name,self.age,self.gender)
p=Person("邹婷","19岁","女")
print(p.personInfo())
class Teacher(Person):
    def __init__(self,college,professional):
        self.college="信息与工程学院"
        self.professional="信息管理与信息系统"
    def personInfo(self):
        print('学院',self.college)
        print('专业',self.professional)  
    def teachObj(self):
        print("今天讲了：面向对象设计程序")
a=Teacher("信息与工程学院","信息管理与信息系统")
a.personInfo()
a.teachObj()
