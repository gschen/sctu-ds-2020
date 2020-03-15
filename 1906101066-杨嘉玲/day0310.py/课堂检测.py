class Student():
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def get_name(self):
        print("姓名：",self.name)
    def get_age(self):
        print("年龄：",self.age)
    def get_course(self):
        print("最高分：",max(self.course))
a=Student("bob",18,[67,56,34])
a.get_name()
a.get_age()
a.get_course()
    


